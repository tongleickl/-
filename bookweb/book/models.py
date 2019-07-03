from django.db import models

# Create your models here.

class Book2(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    style = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    words = models.CharField(max_length=20)
    time = models.DateTimeField()
    latest = models.CharField(max_length=50)

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)
        d = {}
        for attr in fields:
            d[attr] = getattr(self, attr)
        return d

class Book1(models.Model):
    bookname = models.CharField(max_length=50)
    img = models.CharField(max_length=256)
    author = models.CharField(max_length=50)
    words = models.CharField(max_length=50)
    recommend = models.CharField(max_length=50)
    clicks = models.CharField(max_length=50)
    week_recommend = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    latest_chapter = models.CharField(max_length=50)
    latest_introduce = models.CharField(max_length=80)
    last_time = models.CharField(max_length=50)
    introduce = models.CharField(max_length=200)

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)
        d = {}
        for attr in fields:
            d[attr] = getattr(self, attr)
        return d

class Book0(models.Model):
    bookname = models.CharField(max_length=255)
    booksrc = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    words = models.IntegerField()
    recommend = models.IntegerField()
    clicks = models.IntegerField()
    week_recommend = models.IntegerField()
    category = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    latest_chapter = models.CharField(max_length=255)
    latest_introduce = models.CharField(max_length=255)
    last_time = models.CharField(max_length=255)
    introduce = models.CharField(max_length=1000)
    digital_last_time = models.IntegerField()
    score = models.FloatField()

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)
        d = {}
        for attr in fields:
            d[attr] = getattr(self, attr)
        return d

class Comment(models.Model):
    book_id = models.IntegerField()
    content = models.CharField(max_length=255)

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)
        d = {}
        for attr in fields:
            d[attr] = getattr(self, attr)
        return d