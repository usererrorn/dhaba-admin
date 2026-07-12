from django.contrib import admin
from .models import MenuItem, GalleryImage, Location, SiteInfo, FacilityBadge, Perk, Testimonial

admin.site.register(MenuItem)
admin.site.register(GalleryImage)
admin.site.register(Location)
admin.site.register(SiteInfo)
admin.site.register(FacilityBadge)
admin.site.register(Perk)
admin.site.register(Testimonial)