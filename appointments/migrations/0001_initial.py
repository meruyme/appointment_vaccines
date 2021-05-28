# Generated by Django 3.2.3 on 2021-05-28 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome completo')),
                ('birth', models.DateField(verbose_name='Data de nascimento')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('password', models.CharField(max_length=20, verbose_name='Senha')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Grupo de atendimento')),
                ('min_age', models.IntegerField(verbose_name='Idade mínima')),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Vacina')),
                ('manufacturer', models.CharField(max_length=200, verbose_name='Fabricante')),
            ],
        ),
        migrations.CreateModel(
            name='VaccineLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('address', models.CharField(max_length=200, verbose_name='Logradouro')),
                ('neighborhood', models.CharField(max_length=200, verbose_name='Bairro')),
                ('city', models.CharField(max_length=200, verbose_name='Cidade')),
            ],
        ),
    ]
