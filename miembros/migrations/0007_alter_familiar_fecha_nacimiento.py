# Generated by Django 4.0.4 on 2022-05-23 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miembros', '0006_alter_familiar_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]
