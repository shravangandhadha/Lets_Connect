from django.contrib import admin

# Register your models here.

from .models import Member, Message, Call
admin.site.register(Member)
admin.site.register(Message)
admin.site.register(Call)


