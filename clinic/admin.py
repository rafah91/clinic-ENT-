from django.contrib import admin

from .models import Doctor, Clinic, Gallery, PatientReview, BlogPost, LatestNews


class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 1

class ClinicAdmin(admin.ModelAdmin):
    inlines = [GalleryInline]
    list_display = ('name', 'address', 'phone_number', 'email', 'website', 'doctor')
    search_fields = ('name', 'address', 'doctor__name')
    
admin.site.register(Doctor)
admin.site.register(Clinic)
admin.site.register(Gallery)
admin.site.register(PatientReview)
admin.site.register(BlogPost)
admin.site.register(LatestNews)