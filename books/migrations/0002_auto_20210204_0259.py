# Generated by Django 3.1.4 on 2021-02-04 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='address',
            field=models.CharField(blank=True, default='', max_length=30),
            preserve_default=False,
        ),
    ]
