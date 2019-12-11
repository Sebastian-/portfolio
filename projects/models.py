from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    repo_url = models.URLField('Repository URL', blank=True)
    site_url = models.URLField('Site URL', max_length=2000, blank=True)
    image = models.ImageField()
    technologies = models.ManyToManyField(
        'Technology', related_name='projects')


class Technology(models.Model):
    name = models.CharField(max_length=100)
