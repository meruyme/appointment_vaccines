from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from appointments.forms import AutoCreateUserForm, CreateAppointmentForm, SearchAppointmentAvailableForm
from appointments.models import AvailableAppointments, Appointments, ServiceGroup


def create_citizen(request):
    if request.method == 'POST':
        form = AutoCreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            u = authenticate(username=user.email, password=form.cleaned_data.get("password"))
            login(request, u)
            messages.success(request, "O usuário foi cadastrado com sucesso!")
            return redirect('index')
    else:
        form = AutoCreateUserForm()
    context = {
        'form': form
    }
    return render(request, 'create-citizen.html', context=context)


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "O usuário foi desconectado com sucesso!")
    return redirect('index')


def index(request):
    return render(request, 'index.html')


@login_required
def check_appointment(request):
    qs = Appointments.objects.filter(citizen=request.user)
    if not qs.exists():
        if request.method == 'POST':
            form = CreateAppointmentForm(request.user, request, request.POST)
            if form.is_valid():
                request.session['chosen_date'] = form.cleaned_data.get("date_appointment")
                request.session['vaccine'] = form.cleaned_data.get("vaccine").name
                request.session['group'] = form.cleaned_data.get("group").id
                request.session['city'] = form.cleaned_data.get("city").city
                return redirect('realizar_agendamento')
        else:
            form = CreateAppointmentForm(request.user, request)
        print(request.path)
        context = {
            'form': form,
        }
        return render(request, 'create-appointment.html', context=context)
    else:
        messages.error(request, "Você já possui um agendamento feito. Não é possível fazer mais de um agendamento.")
        return redirect('index')


@login_required
def create_appointment(request):
    chosen_date = request.session['chosen_date']
    vaccine = request.session['vaccine']
    id_group = request.session['group']
    city = request.session['city']
    if request.method == 'POST':
        form = SearchAppointmentAvailableForm(chosen_date, vaccine, id_group, city, request.POST)
        if form.is_valid():
            chosen_appointment = form.cleaned_data.get('appointments_available')
            print(chosen_appointment.date_appointment)
            group = ServiceGroup.objects.get(id=id_group)
            a = Appointments(citizen=request.user, group=group, available=chosen_appointment)
            with transaction.atomic():
                chosen_appointment.vacancies -= 1
                chosen_appointment.save(force_update=True)
                a.save()
            request.session.pop('chosen_date')
            request.session.pop('vaccine')
            request.session.pop('group')
            request.session.pop('city')
            request.session.modified = True
            messages.success(request, "O agendamento foi realizado com sucesso!")
            return redirect('index')
    else:
        form = SearchAppointmentAvailableForm(chosen_date, vaccine, id_group, city)
    context = {
        'form': form,
    }
    return render(request, 'create-appointment.html', context=context)


@login_required
def show_appointment(request):
    query = Appointments.objects.filter(citizen=request.user)
    if query.exists():
        data = query[0]
        context = {
            'info': {
                'Dia do agendamento': f"{data.available.date_appointment.strftime('%d/%m/%Y')} "
                                      f"às {data.available.time_appointment.strftime('%H:%M')}",
                'Nome do cidadão': request.user.name,
                'Grupo de atendimento': data.group,
                'Local de vacinação': data.available.location.name,
                'Endereço': f"{data.available.location.address}, bairro {data.available.location.neighborhood}",
                'Cidade': data.available.location.city
            }
        }
        return render(request, 'show-appointment.html', context=context)
    else:
        messages.error(request, "Você ainda não possui agendamentos.")
        return redirect('index')
