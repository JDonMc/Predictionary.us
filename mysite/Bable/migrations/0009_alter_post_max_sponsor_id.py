# Generated by Django 3.2.25 on 2024-08-14 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bable', '0008_alter_post_max_sponsor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='max_sponsor_id',
            field=models.CharField(default='', max_length=200),
        ),
    ]
