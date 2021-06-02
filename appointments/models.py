from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.conf import settings

Citizen = settings.AUTH_USER_MODEL


class UserManager(BaseUserManager):
    def create_user(self, email, name, date_birth, password=None):
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            date_birth=date_birth
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, date_birth, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            date_birth=date_birth,
            password=password
        )
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="E-mail", unique=True)
    name = models.CharField(verbose_name="Nome completo", max_length=200, blank=False)
    date_birth = models.DateField(verbose_name="Data de nascimento", blank=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False, verbose_name="Administrador")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name', 'date_birth']

    objects = UserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ['name']


class VaccineLocation(models.Model):
    cnes = models.CharField(verbose_name="CNES", max_length=200)
    name = models.CharField(verbose_name="Nome", max_length=200)
    address = models.CharField(verbose_name="Logradouro", max_length=200)
    neighborhood = models.CharField(verbose_name="Bairro", max_length=200)
    city = models.CharField(verbose_name="Cidade", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ponto de vacinação"
        verbose_name_plural = "Pontos de vacinação"
        ordering = ['city', 'name']


class Vaccine(models.Model):
    name = models.CharField(verbose_name="Vacina", max_length=200)
    manufacturer = models.CharField(verbose_name="Fabricante", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Vacina"
        verbose_name_plural = "Vacinas"
        ordering = ['name']


class ServiceGroup(models.Model):
    name = models.CharField(verbose_name="Grupo de atendimento", max_length=200)
    min_age = models.IntegerField(verbose_name="Idade mínima")

    def __str__(self):
        return f"{self.name} - {self.min_age} anos"

    class Meta:
        verbose_name = "Grupo de atendimento"
        verbose_name_plural = "Grupos de atendimento"
        ordering = ['name', 'min_age']


class AvailableAppointments(models.Model):
    date_appointment = models.DateField(verbose_name="Data")
    time_appointment = models.TimeField(verbose_name="Horário")
    vacancies = models.IntegerField(verbose_name="Número de vagas")
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE, verbose_name="Vacina")
    location = models.ForeignKey(VaccineLocation, on_delete=models.CASCADE,
                                 verbose_name="Local de vacinação")

    def __str__(self):
        return f"{self.date_appointment} ({self.time_appointment}) - {self.vaccine.name}"

    class Meta:
        verbose_name = "Agendamento disponível"
        verbose_name_plural = "Agendamentos disponíveis"
        ordering = ['date_appointment', 'time_appointment']


class Appointments(models.Model):
    STATUS_CHOICES = (
        ("A", "Agendado"),
        ("C", "Cancelado"),
        ("V", "Vacinado")
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="A")
    available = models.ForeignKey(AvailableAppointments, on_delete=models.CASCADE,
                                  verbose_name="Agendamento escolhido")
    group = models.ForeignKey(ServiceGroup, on_delete=models.CASCADE, verbose_name="Grupo de atendimento")
    citizen = models.OneToOneField(Citizen, on_delete=models.CASCADE, verbose_name="Cidadão")
    date = models.DateField(verbose_name="Data do agendamento", auto_now_add=True)

    def __str__(self):
        return f"{self.citizen.name}: {self.available.__str__()} " \
               f"- {self.group.__str__()}"

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
