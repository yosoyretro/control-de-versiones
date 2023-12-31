# Generated by Django 4.2.2 on 2023-07-25 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_asignaturas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.asignatura')),
            ],
        ),
        migrations.RemoveField(
            model_name='contenido',
            name='id_unidad',
        ),
        migrations.RemoveField(
            model_name='datosinformativos',
            name='horas_trabajos_autonomo',
        ),
        migrations.RemoveField(
            model_name='datosinformativos',
            name='id_unidad',
        ),
        migrations.RemoveField(
            model_name='datosinformativos',
            name='prerequisitos',
        ),
        migrations.RemoveField(
            model_name='datosinformativos',
            name='total_horas_autonomas',
        ),
        migrations.RemoveField(
            model_name='datosinformativos',
            name='total_horas_docencia',
        ),
        migrations.RemoveField(
            model_name='datosinformativos',
            name='total_horas_docente',
        ),
        migrations.RemoveField(
            model_name='datosinformativos',
            name='total_horas_practicas',
        ),
        migrations.DeleteModel(
            name='Subcontenido',
        ),
        migrations.AddField(
            model_name='asignaciones',
            name='id_contenido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.contenido'),
        ),
        migrations.AddField(
            model_name='asignaciones',
            name='id_unidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.unidad'),
        ),
        migrations.AlterField(
            model_name='datosinformativos',
            name='id_asignatura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.asignaciones'),
        ),
    ]
