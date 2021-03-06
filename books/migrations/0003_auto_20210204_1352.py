# Generated by Django 3.1.4 on 2021-02-04 12:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210204_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.publisher'),
        ),
    ]
