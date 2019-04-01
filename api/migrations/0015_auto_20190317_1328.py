# Generated by Django 2.1.7 on 2019-03-17 13:28

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20190314_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bike',
            name='avatar',
        ),
        migrations.AddField(
            model_name='bike',
            name='image',
            field=models.ImageField(default='def.jpg', upload_to=api.models.scramble_uploaded_filename, verbose_name='media'),
        ),
        migrations.AddField(
            model_name='bike',
            name='thumbnail',
            field=models.ImageField(blank=True, default='defthumb.jpg', upload_to='', verbose_name='Thumbnail of uploaded image'),
        ),
        migrations.AddField(
            model_name='bikemodel',
            name='thumbnail',
            field=models.ImageField(blank=True, default='defthumb.jpg', upload_to='', verbose_name='Thumbnail of uploaded image'),
        ),
        migrations.AlterField(
            model_name='bikemodel',
            name='bike_img',
            field=models.ImageField(default='def.jpg', upload_to=api.models.scramble_uploaded_filename, verbose_name='media'),
        ),
    ]
