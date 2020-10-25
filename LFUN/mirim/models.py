from django.db import models

# class Place(models.Model):
#     place_name = models.CharField(max_length=200)
#     place_introduce = models.TextField()
#     place_caution = models.CharField(max_length=200)
#     place_image = models.ImageField(blank=True, upload_to='media/')
#     place_address = models.CharField(max_length = 100)
#     place_postcode = models.CharField(max_length = 100)
#     place_detailAddress = models.CharField(max_length = 100)
#     place_extraAddress = models.CharField(max_length = 100)
#     place_price = models.CharField(max_length = 100)
#     registered_dttm = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return self.place_name


class Funding(models.Model):
    project_name = models.CharField(max_length=200)

    project_introduce = models.TextField() #안올림

    project_category = models.CharField(max_length=200)
    project_image = models.ImageField(blank=True, upload_to='media/')
    funding_price = models.CharField(max_length = 100)
    funded_price = models.CharField(max_length = 100)
    
    # 안올림
    funding_startday = models.CharField(max_length = 100)
    funding_starttime = models.CharField(max_length = 100)

    funding_endday = models.CharField(max_length = 100)
    
    # 안올림
    funding_endtime = models.CharField(max_length = 100)
    project_ticketprice = models.CharField(max_length = 100)
    funding_bank = models.CharField(max_length = 100)
    funding_account = models.CharField(max_length = 100)
    registered_dttm = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name

    def summary(self):
        return self.project_introduce[:100]