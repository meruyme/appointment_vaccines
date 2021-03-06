# Generated by Django 3.2.3 on 2021-05-31 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0010_auto_20210531_1602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointmentroom',
            options={'verbose_name': 'quantidade de vagas para o agendamento', 'verbose_name_plural': 'quantidades de vagas para o agendamento'},
        ),
        migrations.AlterModelOptions(
            name='appointments',
            options={'verbose_name': 'agendamento', 'verbose_name_plural': 'agendamentos'},
        ),
        migrations.AlterModelOptions(
            name='availableappointments',
            options={'ordering': ['date_appointment', 'time_appointment'], 'verbose_name': 'agendamento disponível', 'verbose_name_plural': 'agendamentos disponíveis'},
        ),
        migrations.AlterModelOptions(
            name='servicegroup',
            options={'ordering': ['-name', '-min_age'], 'verbose_name': 'grupo de atendimento', 'verbose_name_plural': 'grupos de atendimento'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['name'], 'verbose_name': 'usuário', 'verbose_name_plural': 'usuários'},
        ),
        migrations.AlterModelOptions(
            name='vaccinationroom',
            options={'ordering': ['name'], 'verbose_name': 'sala de vacinação', 'verbose_name_plural': 'salas de vacinação'},
        ),
        migrations.AlterModelOptions(
            name='vaccine',
            options={'ordering': ['name'], 'verbose_name': 'vacina', 'verbose_name_plural': 'vacinas'},
        ),
        migrations.AlterModelOptions(
            name='vaccinelocation',
            options={'ordering': ['city', 'name'], 'verbose_name': 'ponto de vacinação', 'verbose_name_plural': 'pontos de vacinação'},
        ),
        migrations.AlterField(
            model_name='appointmentroom',
            name='id_appointment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.availableappointments', verbose_name='agendamento disponível'),
        ),
        migrations.AlterField(
            model_name='appointmentroom',
            name='id_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.vaccinationroom', verbose_name='sala de vacinação'),
        ),
        migrations.AlterField(
            model_name='appointmentroom',
            name='vacancies',
            field=models.IntegerField(verbose_name='número de vagas'),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='id_available',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.availableappointments', verbose_name='agendamento escolhido'),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='id_citizen',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='cidadão'),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='id_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.servicegroup', verbose_name='grupo de atendimento'),
        ),
        migrations.AlterField(
            model_name='availableappointments',
            name='date_appointment',
            field=models.DateField(verbose_name='data'),
        ),
        migrations.AlterField(
            model_name='availableappointments',
            name='id_vaccine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.vaccine', verbose_name='vacina'),
        ),
        migrations.AlterField(
            model_name='availableappointments',
            name='time_appointment',
            field=models.TimeField(verbose_name='horário'),
        ),
        migrations.AlterField(
            model_name='servicegroup',
            name='min_age',
            field=models.IntegerField(verbose_name='idade mínima'),
        ),
        migrations.AlterField(
            model_name='servicegroup',
            name='name',
            field=models.CharField(max_length=200, verbose_name='grupo de atendimento'),
        ),
        migrations.AlterField(
            model_name='vaccinationroom',
            name='id_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.vaccinelocation', verbose_name='ponto de vacinação'),
        ),
        migrations.AlterField(
            model_name='vaccinationroom',
            name='name',
            field=models.CharField(max_length=200, verbose_name='sala de vacinação'),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='manufacturer',
            field=models.CharField(max_length=200, verbose_name='fabricante'),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='name',
            field=models.CharField(max_length=200, verbose_name='vacina'),
        ),
        migrations.AlterField(
            model_name='vaccinelocation',
            name='address',
            field=models.CharField(max_length=200, verbose_name='logradouro'),
        ),
        migrations.AlterField(
            model_name='vaccinelocation',
            name='city',
            field=models.CharField(max_length=200, verbose_name='cidade'),
        ),
        migrations.AlterField(
            model_name='vaccinelocation',
            name='name',
            field=models.CharField(max_length=200, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='vaccinelocation',
            name='neighborhood',
            field=models.CharField(max_length=200, verbose_name='bairro'),
        ),
    ]
