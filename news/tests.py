from django.test import TestCase
import datetime as dt

from . models import Editor, Article, tags
# Create your tests here.

class EditorTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.atieno=Editor(firstName='Atieno', lastName='Obwanda',email='atienoobwanda@gmail.com',phone_number='0743068355')


# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.atieno,Editor))

    def test_save_method(self):
        self.atieno.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.atieno= Editor(firstName = 'Atieno', lastName ='Obwanda', email ='atienoobwanda@gmail.com')
        self.atieno.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.atieno)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)    

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)  