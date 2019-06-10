# Generated by Django 2.2.1 on 2019-06-10 02:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0003_auto_20190609_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='pencil',
            name='pencil_img',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='pencilmanufacturer',
            name='manufacturer_img',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='penciltype',
            name='type_img',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_published_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 6, 10, 2, 4, 53, 824555, tzinfo=utc)),
        ),
    ]
