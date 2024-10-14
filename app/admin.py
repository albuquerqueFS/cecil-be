from django.contrib import admin
from app.models import User, Investment, Movement

admin.site.register(Investment)
admin.site.register(Movement)
admin.site.register(User)