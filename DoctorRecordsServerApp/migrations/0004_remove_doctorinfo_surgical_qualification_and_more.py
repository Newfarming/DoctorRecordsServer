# Generated by Django 4.1.1 on 2022-10-12 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorRecordsServerApp', '0003_alter_obtainpatents_get_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorinfo',
            name='surgical_qualification',
        ),
        migrations.AddField(
            model_name='doctorinfo',
            name='surgical_qualification_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='doctorinfo',
            name='surgical_qualification_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='doctorinfo',
            name='surgical_qualification_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='doctorinfo',
            name='surgical_qualification_4',
            field=models.BooleanField(default=False),
        ),
    ]
