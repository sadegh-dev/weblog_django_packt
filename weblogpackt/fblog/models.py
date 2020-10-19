from django.db import models

class Post(models.Model):
    context = models.TextField()
    release_datetime = models.DateTimeField(auto_now_add=True)
    short_link = models.URLField(default="https://www.google.com/")
    count_viewer = models.PositiveIntegerField(null=True)

    def __str__(self):
        return str(self.id) + " | " + self.context

    
    class Meta:
        verbose_name_plural = 'my Posts'
