# Generated by Django 5.1.2 on 2024-10-10 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='interests',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
