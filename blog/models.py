from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    img = models.CharField(max_length=200, blank=False, null=False)
    tags = models.CharField(max_length=300, blank=True, null=True)
    online = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title
     

