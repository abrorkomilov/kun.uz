from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "create_at", "type", "view_count"]
    readonly_fields = ["view_count"]
    search_fields = ["title", "body"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

admin.site.register(Tag)

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ["name", "link"]
    search_fields = ["name"]

admin.site.register(AboutUS)

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ["name", "tel_number", "theme"]
    search_fields = ["name", "theme"]

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["name", "position"]
    