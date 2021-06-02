from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.forms import ModelChoiceField
from django.contrib import messages

from appointments.models import VaccineLocation, Vaccine, ServiceGroup, AvailableAppointments
from datetime import date

User = get_user_model()


class CityModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.city


class AppointmentModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.time_appointment.strftime('%H:%M')} - {obj.location.name}"


def calculate_age(born):
    today = date.today()
    try:
        birthday = born.replace(year=today.year)
    except ValueError:
        birthday = born.replace(year=today.year, month=born.month + 1, day=1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year


class UserAdminCreationForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('name', 'email', 'date_birth', 'is_admin')
        localized_fields = ('date_birth',)

    def clean(self):
        cleaned_data = super(UserAdminCreationForm, self).clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password', error)
        if password and password2 and password != password2:
            self.add_error('password', "As senhas não são iguais.")
            self.add_error('password2', "As senhas não são iguais.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'date_birth', 'is_active', 'is_admin')


class AutoCreateUserForm(UserAdminCreationForm):
    class Meta(UserAdminCreationForm.Meta):
        exclude = ('is_admin',)
        widgets = {
            'date_birth': forms.DateInput(
                format='%d/%m/%Y',
                attrs={'class': 'form-control',
                       'placeholder': 'Selecione uma data',
                       'type': 'date'
                       }),
        }


class CreateAppointmentForm(forms.Form):
    def __init__(self, user, request, *args, **kwargs):
        super(CreateAppointmentForm, self).__init__(*args, **kwargs)
        self.request = request
        self.user = user
        age = calculate_age(self.user.date_birth)
        self.fields['group'] = forms.ModelChoiceField(label='Grupo de atendimento', empty_label=None,
                                                      queryset=ServiceGroup.objects.filter(min_age__lte=age))

    date_appointment = forms.CharField(label='Dia', widget=forms.DateInput(format='%d/%m/%Y',
                                                                           attrs={'class': 'form-control',
                                                                                  'placeholder': 'Selecione uma data',
                                                                                  'type': 'date'
                                                                                  }))
    vaccine = forms.ModelChoiceField(label='Vacina', empty_label=None,
                                     queryset=Vaccine.objects.all().distinct('name'))
    city = CityModelChoiceField(label='Cidade', empty_label=None,
                                queryset=VaccineLocation.objects.all().distinct('city'))

    def clean(self):
        cleaned_data = super(CreateAppointmentForm, self).clean()
        chosen_date = cleaned_data.get("date_appointment")
        vaccine = cleaned_data.get("vaccine").name
        city = cleaned_data.get("city").city
        get_appointments_date = AvailableAppointments.objects.filter(date_appointment=chosen_date,
                                                                     location__city=city,
                                                                     vaccine__name=vaccine,
                                                                     vacancies__gt=0)
        if not get_appointments_date.exists():
            self.add_error('date_appointment', "Não existe um agendamento disponível para esses dados.")
            messages.error(self.request, "Não existe um agendamento disponível para esses dados.")
        return cleaned_data


class SearchAppointmentAvailableForm(forms.Form):
    def __init__(self, chosen_date, vaccine, id_group, city, *args, **kwargs):
        super(SearchAppointmentAvailableForm, self).__init__(*args, **kwargs)
        self.chosen_date = chosen_date
        self.vaccine = vaccine
        self.id_group = id_group
        self.city = city
        get_appointments_date = AvailableAppointments.objects.filter(date_appointment=chosen_date,
                                                                     location__city=city,
                                                                     vaccine__name=vaccine,
                                                                     vacancies__gt=0)
        self.fields['appointments_available'] = AppointmentModelChoiceField(label='Agendamentos disponíveis',
                                                                            empty_label=None,
                                                                            queryset=get_appointments_date)
