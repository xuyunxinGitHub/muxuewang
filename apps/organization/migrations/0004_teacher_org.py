# Generated by Django 2.1.7 on 2019-03-11 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20190311_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='所属机构'),
        ),
    ]