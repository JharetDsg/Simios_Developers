# Generated by Django 4.1.7 on 2023-03-24 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('dni', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('apellidoPaterno', models.CharField(max_length=50)),
                ('apellidoMaterno', models.CharField(max_length=50)),
                ('nombres', models.CharField(max_length=35)),
                ('fechaNacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
                ('tipoUsuario', models.CharField(max_length=10)),
            ],
        ),
    ]
