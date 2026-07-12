from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    is_signature_dish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    caption = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.caption or f"Gallery Image {self.id}"


class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class SiteInfo(models.Model):
    story_heading = models.CharField(max_length=100, default="Our Story")
    story_text = models.TextField()
    whatsapp_number = models.CharField(max_length=20, help_text="Bina + ke, jaise 919999999999")
    contact_display_text = models.CharField(max_length=100, default="GET IN TOUCH")
    contact_phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return "Site Info (Story, WhatsApp, Contact)"

    class Meta:
        verbose_name = "Site Info"
        verbose_name_plural = "Site Info"


class FacilityBadge(models.Model):
    emoji = models.CharField(max_length=10, help_text="Jaise 🛣️ ya 👨‍👩‍👧‍👦")
    label = models.CharField(max_length=100, help_text="Jaise 'National Highway • Open 24/7'")
    order = models.IntegerField(default=0, help_text="Chhota number pehle dikhega")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.emoji} {self.label}"


class Perk(models.Model):
    PAGE_CHOICES = [
        ('truck', 'Truck Page'),
        ('family', 'Family Page'),
    ]
    page = models.CharField(max_length=10, choices=PAGE_CHOICES)
    emoji = models.CharField(max_length=10)
    text = models.CharField(max_length=150)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"[{self.page}] {self.emoji} {self.text}"


class Testimonial(models.Model):
    PAGE_CHOICES = [
        ('truck', 'Truck Page'),
        ('family', 'Family Page'),
    ]
    page = models.CharField(max_length=10, choices=PAGE_CHOICES)
    quote = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"[{self.page}] {self.author}"