from django.db import models
from stdimage.models import StdImageField


class Base(models.Model):
    created = models.DateField('Created', auto_now_add=True)
    modified = models.DateField('Modified', auto_now=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        abstract = True


class Enemy(Base):
    name = models.CharField('Name', max_length=20)
    description = models.CharField('Description', max_length=150)
    image = StdImageField('Image', upload_to='enemies', variations={'thumb': {'width': 480, 'height': 480,
                                                                              'crop': True}})
    facebook_icon = models.CharField('Facebook', max_length=100, default='#')
    twitter_icon = models.CharField('Twitter', max_length=100, default='#')
    instagram_icon = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Enemy'
        verbose_name_plural = 'Enemies'

    def __str__(self):
        return self.name


class Hero(Base):
    name = models.CharField('Name', max_length=20)
    description = models.CharField('Description', max_length=150)
    image = StdImageField('Image', upload_to='heroes', variations={'thumb': {'width': 300, 'height': 300,
                                                                             'crop': True}})

    class Meta:
        verbose_name = 'Hero'
        verbose_name_plural = 'Heroes'

    def __str__(self):
        return self.name


class Price(Base):
    ICON_CHOICES = (
        ('lni-package', 'Package'),
        ('lni-drop', 'Drop'),
        ('lni-star', 'Star'),
    )
    icon = models.CharField('Icon', max_length=15, choices=ICON_CHOICES)
    price = models.CharField('Price', max_length=4)
    title = models.CharField('Title', max_length=10)
    users = models.CharField('Users', max_length=20)
    storage = models.CharField('Storage', max_length=70)
    support = models.CharField('Support', max_length=50)

    class Meta:
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'

    def __str__(self):
        return self.title


class Testimonial(Base):
    name = models.CharField('Name', max_length=15)
    status = models.CharField('Status', max_length=30)
    description = models.CharField('Description', max_length=100)
    image = StdImageField('Image', upload_to='testimonials', variations={'thumb': {'width': 100, 'height': 100,
                                                                                   'crop': True}})

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.name


class Feature(Base):
    ICON_CHOICES = (
        ('lni-rocket', 'Rocket'),
        ('lni-laptop-phone', 'Laptop'),
        ('lni-cog', 'Cog'),
        ('lni-leaf', 'Leaf'),
        ('lni-layers', 'Layers'),
    )

    icon = models.CharField('Icon', max_length=20, choices=ICON_CHOICES)
    title = models.CharField('Title', max_length=50)
    description = models.CharField('Description', max_length=100)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.title


class OtherImage(Base):
    name = models.CharField('Name', max_length=100)
    image = StdImageField('Image', upload_to='other_images', variations={'thumb': {'width': 600, 'height': 670,
                                                                                   'crop': True}})

    class Meta:
        verbose_name = 'Other Image'
        verbose_name_plural = 'Other Images'

    def __str__(self):
        return self.name
