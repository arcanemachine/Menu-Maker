from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from menus_project.constants import RESERVED_KEYWORDS

class Restaurant(models.Model):

    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True, null=True)
    admin_users = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name

    def clean(self):

        # do not allow slugs to be reserved keywords
        if self.slug in RESERVED_KEYWORDS:
            raise ValidationError(
                "This restaurant name is reserved and cannot be used. "\
                "Please choose another name.")

        # do not allow duplicate restaurant slugs
        existing_restaurants_with_same_slug = \
            Restaurant.objects.filter(slug=slugify(self.name))
        if existing_restaurants_with_same_slug.exists() \
            and existing_restaurants_with_same_slug.first() != self \
            and existing_restaurants_with_same_slug.last() != self:
            raise ValidationError("This restaurant name is already in use.")

    def get_absolute_url(self):
        return reverse('restaurants:restaurant_detail',
            kwargs={'restaurant_slug': self.slug })

    def save(self, *args, **kwargs):
        if not self.slug == slugify(self.name):
            self.slug = slugify(self.name)
        self.clean()
        super().save(*args, **kwargs)
