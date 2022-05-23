import datetime as dt
from django.db import models




# Create your models here.

class Editor(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)


    def __str__(self):
        return self.firstName

    class Meta:
        ordering = ['firstName']

    def save_editor(self):
        self.save()

class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    editor = models.ForeignKey(Editor,on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateField(auto_now_add=True)
    # article_image = models.ImageField(upload_to = 'articles/')

    def __str__(self):
        return self.title
    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date = today)
        return news
    
    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date = date)
        return news
    
    # @classmethod
    # def search_by_title(cls,search_term):
    #     news = cls.objects.filter(title__icontains=search_term)
    #     return news
