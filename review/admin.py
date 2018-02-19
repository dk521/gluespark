from django.contrib import admin
from .forms import SignUpForm
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ["id","username","firstname","lastname","email","gender","created_on", "updated_on"]
    #form = SignUpForm
    class Meta:
        model = UserModel

class UserSessionAdmin(admin.ModelAdmin):
    list_display = ["id","user","session_token","is_valid","created_on", "updated_on"]
    #form = SignUpForm
    class Meta:
        model = UserSession

"""
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'shop_id', 'service', 'product_quality', 'delivery_time', 'app_website', 'innovate']
    class Meta:
        model = Review
"""
class ShopPointsAdmin(admin.ModelAdmin):
    list_display = ['id', 'shop', 'reward_points','points_rewarded', 'points_redeemed','points_remaining']
    class Meta:
        model = ShopPoints

"""


admin.site.register(UserModel,UserAdmin)
admin.site.register(UserSession,UserSessionAdmin)

#admin.site.register(Review,ReviewAdmin)
"""
admin.site.register(ShopPoints,ShopPointsAdmin)
