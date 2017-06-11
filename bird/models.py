from django.db import models
from django.contrib.auth.models import User as DjUser
# Create your models here.

class User(models.Model):
    user=models.OneToOneField(DjUser)
    img=models.CharField(max_length = 600)


    def __str__(self): 
     return "%s" % (self.user)



class Update(models.Model):
    text=models.CharField(max_length=250)
    created_on=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User)
    like=models.IntegerField(default=0)
    def __unicode__(self):
        return self.text


class Follows(models.Model):
    user=models.ForeignKey(User,related_name="followsUser")
    follows=models.ForeignKey(User,related_name="followsFollows")

class Fav(models.Model):
    user=models.ForeignKey(User,related_name="posteduser")
    like=models.ForeignKey(User,related_name="like")

