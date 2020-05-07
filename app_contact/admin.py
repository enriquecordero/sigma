from django.contrib import admin
from .models import Apps, Server , Contacts, F5


admin.site.register(Apps)
admin.site.register(Server)
admin.site.register(Contacts)
admin.site.register(F5)

# Register your models here.
