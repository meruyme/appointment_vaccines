# Generated by Django 3.2.3 on 2021-05-31 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0011_auto_20210531_1608'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointmentroom',
            options={'verbose_name': 'Quantidade de vagas para o agendamento', 'verbose_name_plural': 'Quantidades de vagas para o agendamento'},
        ),
        migrations.AlterModelOptions(
            name='appointments',
            options={'verbose_name': 'Agendamento', 'verbose_name_plural': 'Agendamentos'},
        ),
        migrations.AlterModelOptions(
            name='availableappointments',
            options={'ordering': ['date_appointment', 'time_appointment'], 'verbose_name': 'Agendamento disponível', 'verbose_name_plural': 'Agendamentos disponíveis'},
        ),
        migrations.AlterModelOptions(
            name='servicegroup',
            options={'ordering': ['-name', '-min_age'], 'verbose_name': 'Grupo de atendimento', 'verbose_name_plural': 'Grupos de atendimento'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['name'], 'verbose_name': 'Usuário', 'verbose_name_plural': 'Usuários'},
        ),
        migrations.AlterModelOptions(
            name='vaccinationroom',
            options={'ordering': ['name'], 'verbose_name': 'Sala de vacinação', 'verbose_name_plural': 'Salas de vacinação'},
        ),
        migrations.AlterModelOptions(
            name='vaccine',
            options={'ordering': ['name'], 'verbose_name': 'Vacina', 'verbose_name_plural': 'Vacinas'},
        ),
        migrations.AlterModelOptions(
            name='vaccinelocation',
            options={'ordering': ['city', 'name'], 'verbose_name': 'Ponto de vacinação', 'verbose_name_plural': 'Pontos de vacinação'},
        ),
        migrations.AlterField(
            model_name='appointmentroom',
            name='id_appointment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.availableappointments', verbose_name='Agendamento disponível'),
        ),
        migrations.AlterField(
            model_name='appointmentroom',
            name='id_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.vaccinationroom', verbose_name='Sala de vacinação'),
        ),
        migrations.AlterField(
            model_name='appointmentroom',
            name='vacancies',
            field=models.IntegerField(verbose_name='Número de vagas'),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='id_available',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.availableappointments', verbose_name='Agendamento escolhido'),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='id_citizen',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Cidadão'),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='id_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.servicegroup', verbose_name='Grupo de atendimento'),
        ),
        migrations.AlterField(
            model_name='availableappointments',
            name='date_appointment',
            field=models.DateField(verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='availableappointments',
            name='id_vaccine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.vaccine', verbose_name='Vacina'),
        ),
        migrations.AlterField(
            model_name='availableappointments',
            name='time_appointment',
            field=models.TimeField(verbose_name='Horário'),
        ),
        migrations.AlterField(
            model_name='servicegroup',
            name='min_age',
            field=models.IntegerField(verbose_name='Idade mínima'),
        ),
        migrations.AlterField(
            model_name='servicegroup',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Grupo de atendimento'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_birth',
            field=models.DateField(verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Administrador'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nome completo'),
        ),
        migrations.AlterField(
            model_name='vaccinationroom',
            name='id_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.vaccinelocation', verbose_name='Ponto de vacinação'),
        ),
        migrations.AlterField(
            model_name='vaccinationroom',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Sala de vacinação'),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='manufacturer',
            field=models.CharField(max_length=200, verbose_name='Fabricante'),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Vacina'),
        ),
        migrations.AlterField(
            model_name='vaccinelocation',
            name='address',
            field=models.CharField(max_length=200, verbose_name='Logradouro'),
        ),
        migrations.AlterField(
            model_name='vaccinelocation',
            name='city',
            field=models.CharField(max_length=200, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='vaccinelocation',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='vaccinelocation',
            name='neighborhood',
            field=models.CharField(max_length=200, verbose_name='Bairro'),
        ),
    ]