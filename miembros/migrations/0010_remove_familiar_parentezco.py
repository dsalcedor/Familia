# Generated by Django 4.0.4 on 2022-05-25 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miembros', '0009_familiar_fecha_nacimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familiar',
            name='parentezco',
        ),
    ]