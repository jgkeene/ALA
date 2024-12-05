from django.utils import timezone
import datetime
from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns


# Redit data model
class Reddit(models.Model):

    title = models.CharField(max_length=500, null=True, blank=True)
    url = models.URLField(max_length=500, null=True, blank=True)
    num_comments = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True, db_index=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    updated = models.BooleanField(default=False)
#    class Meta:
#        ordering = ["-num_comments"]
    class Meta:
           ordering = ['updated', 'num_comments']

    def get_absolute_url(self):
         return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return '%s, %s, %s, %s, %s, %s' % (
            self.title,
            self.url,
            self.num_comments,
            str(self.date),
            self.author,
            self.updated)
        #    str(self.num_comments) \
        #    + str(self.date)
        #    + self.url \
        #    + str(self.num_comments) \
        #    + str(self.date)

#    def __init__(self, title='', url='', num_comments=0):
#        self.title = title
#        self.url= url
#        self.num_comments = num_comments
#

# Slashdot data model
class Slashdot(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    url = models.URLField(max_length=500, null=True, blank=True)
    num_comments = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True, db_index=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    updated = models.BooleanField(default=False)

    class Meta:
        ordering = ["-num_comments"]

    def get_absolute_url(self):
         return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return '%s, %s, %s, %s, %s, %s' % (
            self.title,
            self.url,
            self.num_comments,
            str(self.date),
            self.author,
            self.updated)
#
#    def __init__(self, title='', url='', num_comments=0):
#        self.title = title
#        self.url= url
#        self.num_comments = num_comments
#

# Hackernews data model
class Hackernews(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    url = models.URLField(max_length=500, null=True, blank=True)
    num_comments = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True, db_index=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    updated = models.BooleanField(default=False)

    class Meta:
        ordering = ["-num_comments"]

    def get_absolute_url(self):
         return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return '%s, %s, %s, %s, %s, %s' % (
            self.title,
            self.url,
            self.num_comments,
            str(self.date),
            self.author,
            self.updated)

