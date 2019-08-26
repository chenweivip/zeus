# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-08-26 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=255, unique=True, verbose_name='账号')),
                ('username', models.CharField(max_length=255, verbose_name='姓名')),
                ('recommend_user', models.CharField(max_length=255, verbose_name='推荐人')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否激活')),
                ('status', models.IntegerField(choices=[(1, '正常'), (2, '冻结')], verbose_name='状态')),
                ('login_password', models.CharField(max_length=255, verbose_name='登陆密码')),
                ('safe_password', models.CharField(max_length=255, verbose_name='安全密码')),
                ('phone', models.CharField(max_length=255, verbose_name='手机号')),
                ('static_money', models.FloatField(default=0, verbose_name='静态钱包')),
                ('dynamic_money', models.FloatField(default=0, verbose_name='动态钱包')),
            ],
        ),
    ]