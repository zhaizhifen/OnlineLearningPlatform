# Generated by Django 2.0.8 on 2018-08-13 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20180813_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='notes',
            field=models.CharField(default='人生苦短，我用Python！', max_length=20, verbose_name='课程须知'),
        ),
    ]