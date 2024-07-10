from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

# from django.contrib.sites.models import Site




# Register your models here.




class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['pk', 'email', 'username', 'first_name', 'last_name', 'ref_id']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('email', 'first_name', 'last_name', 
         'avatar', 'user', 'ref_id')}),
    )

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('avatar','ref_id')}),
        )




class CustomAccount(admin.ModelAdmin):
    list_display = ['pk', 'user', 'profit', 'balance', 'referral' ]
    
    
class CustomProfile(admin.ModelAdmin):
    list_display = ['pk', 'username', 'profit', 'balance', 'referral' ]

    
admin.site.register(CustomUser, CustomUserAdmin)







admin.site.register(Transaction)
# admin.site.register(Account, CustomAccount)
# admin.site.register(Contact)
admin.site.register(Profile, CustomProfile)
admin.site.register(Currency)
admin.site.register(Deposit)
admin.site.register(Withdraw)
admin.site.register(Payment)
admin.site.register(Withdraw_bank)



admin.site.site_header = "Heritage Finance Network"
admin.site.index_title = "Manage Heritage Finance Network"
