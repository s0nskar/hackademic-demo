from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    date_posted = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='created_by')
    last_modified = models.DateTimeField(auto_now_add=True)
    last_modified_by = models.ForeignKey(User, related_name='last_modified_by')
    ordering = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title