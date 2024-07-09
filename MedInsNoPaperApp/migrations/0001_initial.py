# Generated by Django 4.1.3 on 2024-07-01 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedInsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_ins_info', models.TextField(verbose_name='医保详情')),
                ('imgs', models.TextField(verbose_name='图片信息')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=256, verbose_name='账号')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('name', models.CharField(max_length=256, verbose_name='姓名')),
                ('permission_type', models.CharField(max_length=256, verbose_name='权限类型')),
                ('detail_info', models.TextField(verbose_name='账号详情')),
            ],
        ),
    ]