# Generated by Django 2.1.7 on 2019-03-17 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_auto_20190317_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientdetail',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Thumbnail of uploaded image'),
        ),
        migrations.AddField(
            model_name='dealerdetail',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Thumbnail of uploaded image'),
        ),
    ]
