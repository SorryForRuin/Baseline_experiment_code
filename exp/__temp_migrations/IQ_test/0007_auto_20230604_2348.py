# Generated by Django 2.2.12 on 2023-06-04 20:48

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('IQ_test', '0006_auto_20230604_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='likelihood1',
            field=otree.db.models.IntegerField(null=True, verbose_name='Please state in in percent. Do not write percent sign'),
        ),
        migrations.AlterField(
            model_name='player',
            name='likelihood2',
            field=otree.db.models.IntegerField(null=True, verbose_name='Please state in in percent. Do not write percent sign'),
        ),
    ]
