from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return f'{self.id}:{self.title}'