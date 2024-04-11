from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Doctor(models.Model):
    name = models.CharField(_('name'), max_length=100)
    bio = models.TextField(_('bio'))
    photo = models.ImageField(_('photo'), upload_to='doctor_photos/', null=True, blank=True)
    slug = models.SlugField(_('slug'), max_length=100, unique=True, allow_unicode=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Clinic(models.Model):
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100, unique=True, allow_unicode=True, null=True, blank=True)
    address = models.TextField(_('address'))
    phone_number = models.CharField(_('phone number'), max_length=15)
    email = models.EmailField(_('email'))
    website = models.URLField(_('website'), blank=True, null=True)
    opening_hours = models.CharField(_('opening hours'), max_length=100, help_text=_('e.g. Mon-Fri: 9am-5pm'))
    description = models.TextField(_('description'))
    photo = models.ImageField(_('photo'), upload_to='clinic_photos/', null=True, blank=True)
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE, verbose_name=_('doctor'), related_name='clinic')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    clinic = models.OneToOneField(Clinic, on_delete=models.CASCADE, verbose_name=_('clinic'), related_name='gallery')
    # Add any additional fields you may need for your gallery

    def __str__(self):
        return f"Gallery of {self.clinic.name}"

class PatientReview(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, verbose_name=_('clinic'), related_name='patient_reviews')
    patient_name = models.CharField(_('patient name'), max_length=100)
    review = models.TextField(_('review'))

    def __str__(self):
        return f"{self.patient_name}'s review for {self.clinic.name}"

class BlogPost(models.Model):
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'), max_length=200, unique=True, allow_unicode=True)
    content = models.TextField(_('content'))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class LatestNews(models.Model):
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'), max_length=200, unique=True, allow_unicode=True)
    content = models.TextField(_('content'))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title