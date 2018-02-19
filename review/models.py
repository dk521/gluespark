from django.db import models
#from registration.forms import Registration
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.


class UserModel(models.Model):
    firstname = models.CharField(max_length = 30)
    lastname = models.CharField(max_length = 30)
    username = models.CharField(max_length = 20, null=False, blank=False)
    email = models.EmailField(max_length=50, unique=True, null=False, blank=False)
    gender = models.CharField(max_length=7)
    password = models.CharField(max_length=40)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

class UserSession(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.PROTECT)
    session_token = models.CharField(max_length=255)
    is_valid = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def create_session_token(self):
        from uuid import uuid4

        self.session_token = uuid4()


class ShopPoints(models.Model):
    shop = models.ForeignKey(User, on_delete=models.PROTECT)
    reward_points = models.IntegerField(default=0)
    points_rewarded = models.IntegerField(default=0)
    points_redeemed = models.IntegerField(default=0)
    points_remaining = models.IntegerField(default=0)

"""
class Review(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    shop_id = models.ForeignKey(ShopAvailable, on_delete=models.CASCADE)

    service = models.FloatField(default=0.0)
    product_quality = models.FloatField(default=0.0)
    delivery_time = models.FloatField(default=0.0)
    app_website = models.FloatField(default=0.0)
    innovate = models.BooleanField(default=False)
    #innovative_idea = models.CharField(max_length=500)



"""