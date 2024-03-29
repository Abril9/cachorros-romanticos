# Generated by Django 4.0.6 on 2022-07-20 02:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_remove_usuario_fecha_alta'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='fecha_alta',
            field=models.DateTimeField(default=django.utils.timezone.get_current_timezone),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pais_alias',
            field=models.ForeignKey(default='AR', on_delete=django.db.models.deletion.PROTECT, to='aplicacion.pais'),
        ),
    ]
