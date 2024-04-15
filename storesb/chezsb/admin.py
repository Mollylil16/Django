from django.contrib import admin
from .models import *

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Contact)
admin.site.register(Client)
