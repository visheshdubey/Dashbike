# Generated by Django 2.1.7 on 2019-04-06 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190406_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('cancelled', 'cancelled'), ('booked', 'booked'), ('pending', 'pending')], default='pending', max_length=20),
        ),
    ]
