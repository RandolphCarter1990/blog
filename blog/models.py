from django.db import models
from django.shortcuts import render, get_object_or_404
from froala_editor.fields import FroalaField
from image_cropping import ImageRatioField
import os


# Create your models here.


class Article (models.Model):
    title = models.CharField(max_length=128, verbose_name = "Название статьи")
    pub_date = models.DateField(verbose_name = "Дата публикации")
    category = models.ManyToManyField('blog.Category', blank=True , verbose_name = "Категория")
    visits = models.IntegerField('Просмотров', editable = True, default = 0)
    content = FroalaField(theme='black')
    preview_text = models.TextField('Предпросмотр текста',max_length=537)

    def dayabbr(self):
        return self.pub_date.strftime('%d')

    def monthabbr(self):
        return self.pub_date.strftime('%b')   

    def id(self):
        return self.id 

    def get_upload_path(self,filename):
        return os.path.join('static/blog/articles', str(self.id),filename)      


    cover_image = models.ImageField('Заглавная картинка', upload_to = get_upload_path, blank = 'True') 
    cover_cropping = ImageRatioField('cover_image', '1252x754')

    preview_image_1 = models.ImageField('Предпросмотр 1', upload_to = get_upload_path, blank = 'True')
    preview_image_1_cropping = ImageRatioField('preview_image_1', '150x150') 

    preview_image_2 = models.ImageField('Предпросмотр 2', upload_to = get_upload_path, blank = 'True') 
    preview_image_2_cropping = ImageRatioField('preview_image_2', '150x150') 

    preview_image_3 = models.ImageField('Предпросмотр 3', upload_to = get_upload_path, blank = 'True')
    preview_image_3_cropping = ImageRatioField('preview_image_3', '150x150') 

    preview_image_4 = models.ImageField('Предпросмотр 4', upload_to = get_upload_path, blank = 'True')  
    preview_image_4_cropping = ImageRatioField('preview_image_4', '150x150') 

    

    def __str__ (self):
        return self.title 

       

class Category (models.Model):
    title = models.CharField(max_length=10)
    popularity = models.IntegerField('Просмотров', editable = True, default = 0)

    def __str__ (self):
        return self.title

    