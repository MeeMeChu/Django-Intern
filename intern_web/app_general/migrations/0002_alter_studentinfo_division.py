# Generated by Django 4.2.7 on 2023-11-13 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_general', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='division',
            field=models.CharField(choices=[('ICT', 'Information and Communication Technology'), ('CS', 'Computer Science')], max_length=60),
        ),
    ]
