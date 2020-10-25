from django.db import models

class Place(models.Model):
    place_name = models.CharField(max_length=200)
    place_introduce = models.TextField()
    place_caution = models.CharField(max_length=200)
    place_image = models.ImageField(blank=True, upload_to='media/')
    place_address = models.CharField(max_length = 100)
    place_postcode = models.CharField(max_length = 100)
    place_detailAddress = models.CharField(max_length = 100)
    place_extraAddress = models.CharField(max_length = 100)
    place_price = models.CharField(max_length = 100)
    registered_dttm = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.place_name

