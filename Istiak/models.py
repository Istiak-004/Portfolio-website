from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    body = RichTextUploadingField(null=True,blank=True)
    upload_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag ,blank=True)
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        
        if self.slug==None:
            slug = slugify(self.title)
            has_slug = Blog.objects.filter(slug = slug).exists()
            count = 1

            while has_slug:
                count +=1
                slug = slugify(self.title)+ '-' + str(count)
                has_slug = Blog.objects.filter(slug = slug).exists()
            
            self.slug = slug
        super().save(*args,**kwargs)
    


    

