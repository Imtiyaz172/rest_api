from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .import models

class indexSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    def items(self):
        return ['index']
    def location(self, item):
        return reverse(item)

class aboutSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    def items(self):
        return ['about']
    def location(self, item):
        return reverse(item)

class contactSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    def items(self):
        return ['contact']
    def location(self, item):
        return reverse(item)

class loginSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    def items(self):
        return ['login']
    def location(self, item):
        return reverse(item)

class registerSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    def items(self):
        return ['register']
    def location(self, item):
        return reverse(item)

class dashboardSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    def items(self):
        return ['dashboard']
    def location(self, item):
        return reverse(item)

class historySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    def items(self):
        return ['history']
    def location(self, item):
        return reverse(item)

class classSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return models.classes.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.update

class subjectSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return models.classsubject.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.classes.update

class questionSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return models.question.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.lastmod