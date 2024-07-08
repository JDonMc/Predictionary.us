# Generated by Django 3.2.25 on 2024-07-07 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bable', '0003_auto_20240701_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.TextField(default='', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='pageviews',
            name='ip_addresses',
            field=models.ManyToManyField(default=None, to='Bable.IpAddress'),
        ),
    ]