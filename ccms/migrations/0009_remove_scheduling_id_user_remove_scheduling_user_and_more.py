# Generated by Django 5.0.3 on 2024-05-21 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccms', '0008_scheduling_id_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduling',
            name='id_user',
        ),
        migrations.RemoveField(
            model_name='scheduling',
            name='user',
        ),
        migrations.AlterField(
            model_name='scheduling',
            name='case_date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='scheduling',
            name='case_number',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='scheduling',
            name='case_time',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='scheduling',
            name='case_title',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='scheduling',
            name='judged',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
