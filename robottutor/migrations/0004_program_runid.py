# Generated by Django 3.2.6 on 2021-09-11 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robottutor', '0003_auto_20210902_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='runid',
            field=models.IntegerField(null=True),
        ),
    ]
