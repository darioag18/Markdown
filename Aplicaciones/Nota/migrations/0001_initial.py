# Generated by Django 3.2.8 on 2022-02-21 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('idNota', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=75)),
                ('contenido', models.CharField(max_length=2000)),
                ('propietario', models.CharField(max_length=20)),
            ],
        ),
    ]
