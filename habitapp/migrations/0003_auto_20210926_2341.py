# Generated by Django 3.1.4 on 2021-09-26 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitapp', '0002_habitmodel_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitmodel',
            name='good_or_bad',
            field=models.CharField(choices=[('good', '良い習慣'), ('bad', '悪い習慣'), ('normal', '日常習慣')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='habitmodel',
            name='time',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='habitmodel',
            name='frequency',
            field=models.CharField(choices=[('year', '1年'), ('month', '1ヶ月'), ('week', '1週間'), ('day', '1日')], max_length=10, null=True),
        ),
    ]