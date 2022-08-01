from django.db import models

class Articles(models.Model):
    title = models.CharField('Title', max_length=100)
    announcement = models.CharField('Announcement', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= 'New'
        verbose_name_plural= 'News'
