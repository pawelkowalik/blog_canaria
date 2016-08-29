# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from .models import News


class ArchieveFeed(Feed):
    title = 'Wczasy na Krecie'
    description = 'Czyli Kasia i Paweł na wakacjach'
    link = '/archieve/'

    def items(self):
        return News.objects.order_by('-posted_date')[:10]

    def item_link(self, item):
        return '/news/'+item.slug

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

