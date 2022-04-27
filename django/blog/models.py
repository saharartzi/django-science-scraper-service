from django.db import models
from django.utils import timezone
from django.conf import settings



class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    authors = models.CharField(max_length=250,null=True)
    date = models.CharField(max_length=15, null=True)
    link = models.TextField(null=True)
    details = models.TextField(null=True)
    cites = models.IntegerField(null=True)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    scraper = models.ForeignKey(
        settings.SCRAPER_MODEL, on_delete=models.CASCADE, related_name='scraper_posts',null=True )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts',null=True)
    status = models.CharField(
        max_length=10, choices=options, default='published')

    # object manegers configuration
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
