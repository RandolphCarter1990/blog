from django.contrib import admin
from image_cropping import ImageCroppingMixin

from .models import Article
from .models import Category


admin.site.register(Category)
class ImageCropAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Article,ImageCropAdmin)
