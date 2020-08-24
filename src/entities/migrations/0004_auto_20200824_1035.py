# Generated by Django 2.2.15 on 2020-08-24 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0003_movement_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='covidpipe',
            name='con_muestra',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='covidpipe',
            name='last_movement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_movement', to='entities.Movement'),
        ),
        migrations.AlterField(
            model_name='movement',
            name='pipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movement', to='entities.CovidPipe'),
        ),
    ]