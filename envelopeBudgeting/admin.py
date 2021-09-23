from django.contrib import admin

# Register your models here.
from .models import Envelope, Transaction

admin.site.register(Envelope)
admin.site.register(Transaction)