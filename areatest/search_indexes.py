# -*- coding: UTF-8 -*-
from haystack import indexes
from .models import Index


class GoodsInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Index

    def index_queryset(self, using=None):
        return self.get_model().objects.all()