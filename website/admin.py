from django.contrib import admin
from .models import Service, ServiceDetail, BlogPost, Comment, AppUser

# Register your models here.

class ServiceDetailAdmin(admin.ModelAdmin):
    list_display = ("name", "price",)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "date_posted",)

admin.site.register(Service)

admin.site.register(Comment)
admin.site.register(AppUser)
admin.site.register(ServiceDetail, ServiceDetailAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
