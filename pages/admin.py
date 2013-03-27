from django.contrib import admin
from pages.models import Page, Navig, Img, Cont, Sect

class ChoiceInline(admin.StackedInline):
    model = Navig, Img, Cont, Sect
    extra = 5
	
class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date')	
	
admin.site.register(Navig)
admin.site.register(Img)
admin.site.register(Cont)
admin.site.register(Sect)	
admin.site.register(Page)


