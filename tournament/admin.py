from django.contrib import admin
from .models import Enemy, Hero, Price, Testimonial, Feature, OtherImage


@admin.register(Enemy)
class EnemyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created', 'modified', 'active')


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created', 'modified', 'active')


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'users', 'storage', 'support', 'created', 'modified', 'active')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'description', 'created', 'modified', 'active')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(OtherImage)
class OtherImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

