from django.contrib import admin
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken
from allauth.account.models import EmailAddress
from .models import Schedule

# Register your models here.

admin.site.register(Schedule)

# Unregister models 
admin.site.unregister(Site)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(SocialToken)
admin.site.unregister(EmailAddress)