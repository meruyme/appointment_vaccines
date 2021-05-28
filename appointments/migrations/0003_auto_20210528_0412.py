# Generated by Django 3.2.3 on 2021-05-28 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_vaccinelocation_cnes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='citizen',
            options={'verbose_name': 'Cidadão', 'verbose_name_plural': 'Cidadãos'},
        ),
        migrations.AlterModelOptions(
            name='servicegroup',
            options={'verbose_name': 'Grupo de atendimento', 'verbose_name_plural': 'Grupos de atendimento'},
        ),
        migrations.AlterModelOptions(
            name='vaccine',
            options={'verbose_name': 'Vacina', 'verbose_name_plural': 'Vacinas'},
        ),
        migrations.AlterModelOptions(
            name='vaccinelocation',
            options={'verbose_name': 'Ponto de vacinação', 'verbose_name_plural': 'Pontos de vacinação'},
        ),
        migrations.CreateModel(
            name='VaccinationRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Sala')),
                ('id_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.vaccinelocation', verbose_name='Ponto de vacinação')),
            ],
            options={
                'verbose_name': 'Sala de vacinação',
                'verbose_name_plural': 'Salas de vacinação',
            },
        ),
        migrations.CreateModel(
            name='AvailableAppointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_appointment', models.DateField(verbose_name='Data')),
                ('time_appointment', models.TimeField(verbose_name='Horário')),
                ('id_vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.vaccine', verbose_name='Vacina')),
            ],
            options={
                'verbose_name': 'Agendamento disponível',
                'verbose_name_plural': 'Agendamentos disponíveis',
            },
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('A', 'Agendado'), ('C', 'Cancelado'), ('V', 'Vacinado')], default='A', max_length=1)),
                ('id_available', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.availableappointments', verbose_name='Agendamento escolhido')),
                ('id_citizen', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appointments.citizen', verbose_name='Cidadão')),
                ('id_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.servicegroup', verbose_name='Grupo de atendimento')),
            ],
            options={
                'verbose_name': 'Agendamento',
                'verbose_name_plural': 'Agendamentos',
            },
        ),
    ]