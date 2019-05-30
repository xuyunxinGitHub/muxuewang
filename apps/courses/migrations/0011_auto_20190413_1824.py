# Generated by Django 2.1.7 on 2019-04-13 18:24

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_course_is_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerCourse',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name': '轮播课程',
                'indexes': [],
                'verbose_name_plural': '轮播课程',
            },
            bases=('courses.course',),
        ),
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('cj', '初级'), ('zj', '中级'), ('gj', '高级')], default='cj', max_length=2, verbose_name='难度'),
        ),
        migrations.AlterField(
            model_name='course',
            name='desc',
            field=models.CharField(default='', max_length=300, verbose_name='课程描述'),
        ),
        migrations.AlterField(
            model_name='course',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='课程详情'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='', upload_to='course/%Y/%m/%d/', verbose_name='封面图'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='课程名'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='章节名'),
        ),
    ]
