# Generated by Django 3.2.25 on 2024-08-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bable', '0003_auto_20240802_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='anon',
            name='example_sort_char',
            field=models.CharField(choices=[('the_example_itself', 'Alphabetical'), ('-the_example_itself', 'Backwards Alpha'), ('word_count', 'Most Words'), ('-word_count', 'Least Words'), ('dictionary_count', 'Most Dics'), ('-dictionary_count', 'Least Dics'), ('comment_count', 'Most Comments'), ('-comment_count', 'Least Comments'), ('views', 'Most Viewed'), ('-views', 'Most Viewed')], default='latest_change_date', max_length=180),
        ),
        migrations.AddField(
            model_name='anon',
            name='sponsor_sort_char',
            field=models.CharField(choices=[('the_sponsorship_phrase', 'Alphabetical'), ('-the_sponsorship_phrase', 'Reverse Alphabetical'), ('latest_change_date', 'Least Recent Change'), ('-latest_change_date', 'Most Recent Change'), ('price_limit', 'Price Limit'), ('-price_limit', 'Affordability Limit'), ('allowable_expenditure', 'Most Expenditure'), ('-allowable_expenditure', 'Least Expenditure'), ('votes_count', 'Most Votes'), ('-votes_count', 'Least Votes'), ('views', 'Most Views'), ('-views', 'Least Views')], default='latest_change_date', max_length=180),
        ),
        migrations.AddField(
            model_name='example',
            name='comment_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='example',
            name='dictionary_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='example',
            name='word_count',
            field=models.IntegerField(default=0),
        ),
    ]
