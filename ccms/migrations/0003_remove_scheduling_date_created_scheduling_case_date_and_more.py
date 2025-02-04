# Generated by Django 4.2.2 on 2023-10-30 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccms', '0002_scheduling'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduling',
            name='date_created',
        ),
        migrations.AddField(
            model_name='scheduling',
            name='case_date',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scheduling',
            name='case_time',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='scheduling',
            name='judged',
            field=models.CharField(max_length=100),
        ),
    ]
