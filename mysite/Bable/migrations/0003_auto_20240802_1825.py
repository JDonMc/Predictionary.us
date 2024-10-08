# Generated by Django 3.2.25 on 2024-08-02 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bable', '0002_invoice_price_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='max_sponsor_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='max_sponsor_img',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='post',
            name='max_sponsor_url',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
    ]
