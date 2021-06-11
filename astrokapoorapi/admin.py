from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Seller)
admin.site.register(CategoryService)

admin.site.register(Birth)
admin.site.register(ContactDetail)

