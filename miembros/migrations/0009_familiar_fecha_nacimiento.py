# Generated by Django 4.0.4 on 2022-05-23 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miembros', '0008_remove_familiar_fecha_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]