# Generated by Django 3.2.3 on 2021-05-31 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0009_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_birth',
            field=models.DateField(verbose_name='data de nascimento'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='administrador'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200, verbose_name='nome completo'),
        ),
    ]
