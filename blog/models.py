"""from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

#build the object
#Post is a Django Model, so that Django will know it should be saved in the database
class Post(models.Model): 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) # text with limited number of characters
    #TextField is long text without a limit
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now) # for data and time
    published_date = models.DateTimeField(blank=True, null=True)
    #ForeignKey is for linking to another model
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title"""

from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    