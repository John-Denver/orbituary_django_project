from django.contrib.sitemaps import Sitemap
from .models import Obituary
from django.urls import reverse

class ObituarySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Obituary.objects.all()

    def lastmod(self, obj):
        return obj.submission_date

    def location(self, obj):
        return reverse('view_obituaries') 
