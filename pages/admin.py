from django.contrib import admin
from pages.models import Page, Choice

admin.site.register(Choice)
class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'pub_date')

admin.site.register(Page, PageAdmin)
