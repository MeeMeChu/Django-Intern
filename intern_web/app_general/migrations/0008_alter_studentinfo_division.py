# Generated by Django 4.2.7 on 2023-11-14 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_general', '0007_alter_studentinfo_division'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='division',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_general.division'),
        ),
    ]