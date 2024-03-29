from django.db import models
from Users.models import CustomUser, ClientDetail, DealerDetail
from django.contrib.auth import get_user_model
from django.utils import timezone
import io
from django.core.files.storage import default_storage as storage

# Create your models here.

import uuid
import os
from django.conf import settings
from PIL import Image


def scramble_uploaded_filename(instance, filename):

    extension = filename.split(".")[-1]
    return "media/bikes/{}.{}".format(uuid.uuid4(), extension)

# creates a thumbnail of an existing image


def create_thumbnail(input_image, thumbnail_size=(256, 256)):

    if not input_image or input_image == "":
        return
    img_read = storage.open(input_image.name, 'rb')
    img = Image.open(img_read)

    # use PILs thumbnail method; use anti aliasing to make the scaled picture look good
    img.thumbnail(thumbnail_size, Image.ANTIALIAS)
    in_mem_file = io.BytesIO()
    # parse the filename and scramble it
    print(storage.open(input_image.name))
    new_filename = "thumb_"+str(storage.open(input_image.name))

    # save the image in Amazon S3 and return the filename
    img.save(in_mem_file, format='PNG')
    img_write = storage.open(new_filename, 'w+')
    img_write.write(in_mem_file.getvalue())
    img_write.close()
    img_read.close()

    return new_filename


class Bike(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bike_name = models.CharField(max_length=500, default=None)
    image = models.ImageField(
        "media", upload_to=scramble_uploaded_filename, default='def.jpg')
    thumbnail = models.ImageField(
        "Thumbnail of uploaded image", blank=True, default='defthumb.jpg')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.thumbnail = create_thumbnail(self.image)

        super(Bike, self).save(*args, **kwargs)

    def __str__(self):
        return self.bike_name


class BikeModel(models.Model):
    bike_model = models.ForeignKey(
        'Bike', on_delete=models.PROTECT, default=None)
    dealer = models.ForeignKey(
        DealerDetail, on_delete=models.CASCADE, default=None)
    description = models.CharField(max_length=500, default=None)
    count = models.IntegerField(default=0)
    bike_rate_hr = models.CharField(max_length=500, null=True, blank=True)
    bike_rate_h = models.CharField(max_length=500, null=True, blank=True)
    bike_rate_f = models.CharField(max_length=500, null=True, blank=True)
    bike_isAvailable = models.BooleanField(default=True)
    isActive = models.BooleanField(default=True)

    def bike_model_id(self):
        return str(self.bike_model.bike_model.id)

    def bike_img(self):
        return self.bike_model.image

    def thumbnail(self):
        return self.bike_model.thumbnail

    def __str__(self):

        return str(self.bike_model)


class Booking(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bike_model = models.ForeignKey(
        'BikeModel', on_delete=models.CASCADE, default=None)
    pickup_time = models.DateTimeField(default=None)
    booking_time = models.DateTimeField(default=None)
    duration = models.CharField(max_length=500, default=0.0)
    client = models.ForeignKey(
        ClientDetail, on_delete=models.CASCADE, default=None)
    dealer = models.ForeignKey(
        DealerDetail, on_delete=models.CASCADE, default=None)
    transaction_amt = models.CharField(
        max_length=500, default=0.0)  # change name
    ord_id = models.CharField(max_length=500, default=0.0)
    transaction_id = models.CharField(max_length=500, default=0.0)
    booking_status = (
        ('cancelled', 'cancelled'),
        ('failed', 'failed'),
        ('booked', 'booked'),
        ('pending', 'pending'),
    )
    status = models.CharField(
        max_length=20, choices=booking_status, default='pending')
    unit_duration = (
        ('hrs', 'hrs'),
        ('half_day', 'half_day'),
        ('full_day', 'full_day'),
    )
    duration_unit = models.CharField(
        max_length=20, choices=unit_duration, default='hrs')

    def __str__(self):
        return str(self.bike_model.dealer)

    def dealer_name(self):
        return str(self.bike_model.dealer.type.username)

    def bike_model_name(self):
        return str(self.bike_model.bike_model.bike_name)
