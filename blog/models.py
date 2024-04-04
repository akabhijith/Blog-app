from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User #users are going to auther a post.1-to-many reln.
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now())
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) : #how it should be printed out or shown in the ORM
        return self.title
    
    def get_absolute_url(self):#so that django knows the location of a specific route
        return reverse("post-detail", kwargs={"pk": self.pk})#reverse returns the full url to the route as a string
                                                            #so in this case the view will handle the redirect for us
    