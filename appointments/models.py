from django.db import models
# TODO: verificar relacionamento n:n de sala com agendamento, creio que não precisa de uma nova tabela


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


class Vaccine(models.Model):
    name = models.CharField(verbose_name="Vacina", max_length=200)
    manufacturer = models.CharField(verbose_name="Fabricante", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Vacina"
        verbose_name_plural = "Vacinas"


class Citizen(models.Model):
    name = models.CharField(verbose_name="Nome completo", max_length=200)
    birth = models.DateField(verbose_name="Data de nascimento")
    email = models.EmailField(verbose_name="E-mail")
    password = models.CharField(verbose_name="Senha", max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Cidadão"
        verbose_name_plural = "Cidadãos"


class ServiceGroup(models.Model):
    name = models.CharField(verbose_name="Grupo de atendimento", max_length=200)
    min_age = models.IntegerField(verbose_name="Idade mínima")

    def __str__(self):
        return f"{self.name} - {self.min_age} anos"

    class Meta:
        verbose_name = "Grupo de atendimento"
        verbose_name_plural = "Grupos de atendimento"


class AvailableAppointments(models.Model):
    date_appointment = models.DateField(verbose_name="Data")
    time_appointment = models.TimeField(verbose_name="Horário")
    id_vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE, verbose_name="Vacina")

    def __str__(self):
        return f"{self.date_appointment} ({self.time_appointment}) - {self.id_vaccine.name}"

    class Meta:
        verbose_name = "Agendamento disponível"
        verbose_name_plural = "Agendamentos disponíveis"


class Appointments(models.Model):
    STATUS_CHOICES = (
        ("A", "Agendado"),
        ("C", "Cancelado"),
        ("V", "Vacinado")
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="A")
    id_available = models.ForeignKey(AvailableAppointments, on_delete=models.CASCADE,
                                     verbose_name="Agendamento escolhido")
    id_group = models.ForeignKey(ServiceGroup, on_delete=models.CASCADE, verbose_name="Grupo de atendimento")
    id_citizen = models.OneToOneField(Citizen, on_delete=models.CASCADE, verbose_name="Cidadão")

    def __str__(self):
        return f"{self.id_citizen.name}: {self.id_available.__str__()} " \
               f"- {self.id_group.__str__()}"

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"


class VaccinationRoom(models.Model):
    name = models.CharField(verbose_name="Sala", max_length=200)
    id_location = models.ForeignKey(VaccineLocation, on_delete=models.CASCADE, verbose_name="Ponto de vacinação")

    def __str__(self):
        return f"{self.name} - {self.id_location.__str__()}"

    class Meta:
        verbose_name = "Sala de vacinação"
        verbose_name_plural = "Salas de vacinação"

