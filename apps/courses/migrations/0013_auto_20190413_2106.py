# Generated by Django 2.1.7 on 2019-04-13 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20190413_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.CharField(blank=True, default='后端开发', max_length=20, null=True, verbose_name='课程类别'),
        ),
    ]
