from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# from django.contrib.auth.admin import GroupAdmin
# from django.contrib.auth.models import User, Group
#
#
# class UserSetInline(admin.TabularInline):
#     model = User.groups.through
#     # raw_id_fields = ('user',)  # optional, if you have too many users
#
#
# class MyGroupAdmin(GroupAdmin):
#     inlines = [UserSetInline]
#
#
# # unregister and register again
# admin.site.unregister(Group)
# admin.site.register(Group, MyGroupAdmin)
admin.site.register(User, UserAdmin)