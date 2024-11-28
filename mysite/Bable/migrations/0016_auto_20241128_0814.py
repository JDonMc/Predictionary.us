# Generated by Django 3.2.25 on 2024-11-28 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bable', '0015_auto_20241128_0640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='minecraftserver',
            old_name='game_modes',
            new_name='game_models',
        ),
        migrations.AddField(
            model_name='angelnumber',
            name='max_sponsor_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='angelnumber',
            name='max_sponsor_img',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='angelnumber',
            name='max_sponsor_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='angelnumber',
            name='max_sponsor_url',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='anon',
            name='max_sponsor_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='anon',
            name='max_sponsor_img',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='anon',
            name='max_sponsor_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='anon',
            name='max_sponsor_url',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='barcode',
            name='max_sponsor_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='barcode',
            name='max_sponsor_img',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='barcode',
            name='max_sponsor_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='barcode',
            name='max_sponsor_url',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='comment',
            name='max_sponsor_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='comment',
            name='max_sponsor_img',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='comment',
            name='max_sponsor_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='max_sponsor_url',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='definition',
            name='max_sponsor_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='definition',
            name='max_sponsor_img',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='definition',
            name='max_sponsor_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='definition',
            name='max_sponsor_url',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='dictionary',
            name='max_sponsor_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='dictionary',
            name='max_sponsor_img',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='dictionary',
            name='max_sponsor_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dictionary',
            name='max_sponsor_url',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='job',
            name='max_sponsor_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='job',
            name='max_sponsor_img',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='job',
            name='max_sponsor_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='max_sponsor_url',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='max_sponsor_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='max_sponsor_img',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='max_sponsor_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='max_sponsor_url',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='post',
            name='max_sponsor_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='price',
            name='max_sponsor_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='price',
            name='max_sponsor_img',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='price',
            name='max_sponsor_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='price',
            name='max_sponsor_url',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='searchurl',
            name='max_sponsor_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='searchurl',
            name='max_sponsor_img',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='searchurl',
            name='max_sponsor_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='searchurl',
            name='max_sponsor_url',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='space',
            name='max_sponsor_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='space',
            name='max_sponsor_img',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='space',
            name='max_sponsor_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='space',
            name='max_sponsor_url',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='userspecificjavascriptvariableviewlearning',
            name='max_sponsor_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='userspecificjavascriptvariableviewlearning',
            name='max_sponsor_img',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='userspecificjavascriptvariableviewlearning',
            name='max_sponsor_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userspecificjavascriptvariableviewlearning',
            name='max_sponsor_url',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='votings',
            name='max_sponsor_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='votings',
            name='max_sponsor_img',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='votings',
            name='max_sponsor_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='votings',
            name='max_sponsor_url',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='word',
            name='max_sponsor_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='word',
            name='max_sponsor_img',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='word',
            name='max_sponsor_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='word',
            name='max_sponsor_url',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
    ]