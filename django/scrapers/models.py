from django.db import models
from django.conf import settings

class Website(models.Model):

    class Meta:
          app_label  = 'scrapers'

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Scraper(models.Model):

    class Meta:
        app_label  = 'scrapers'

    name = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    website = models.ForeignKey(Website, on_delete=models.CASCADE, default=1)
    key_words = models.CharField(max_length=60, null=True)# for example: "coral+genetics+algea"
    years_to_search = models.CharField(max_length=60, null=True)
    slug = models.SlugField(max_length=250, unique=user.name)
    
    objects = models.Manager()

class Doi(models.Model):

    class Meta:
        app_label  = 'scrapers'

    website = "SciHub"
    doi = models.CharField(max_length=60)
    link = models.CharField(max_length=60,default='no link to this article')