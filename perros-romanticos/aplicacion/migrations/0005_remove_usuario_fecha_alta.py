# Generated by Django 4.0.6 on 2022-07-20 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_usuario_fecha_alta_alter_usuario_pais_alias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='fecha_alta',
        ),
    ]
