from django.db import models


class AreaInfo(models.Model):
    atitle = models.CharField(max_length=20)
    parea = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.atitle

    class Meta(object):
        db_table = 'areas'

class Index(models.Model):
    content = models.CharField(max_length=1000)
    class Meta(object):
        db_table = 'index'
