# Generated by Django 3.2.25 on 2024-08-05 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bable', '0007_auto_20240804_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='max_sponsor_id',
            field=models.CharField(default='1', max_length=200),
        ),
    ]
