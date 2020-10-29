from django.db import models
from datetime import datetime

# Create your models here.
class ShowManager (models.Manager):
    def validate_data(self, postData):
        errors = {}
        if len(postData['title_txt']) < 2:
            errors["title"] = "Movie title should be at least 2 characters long."
        else:
            try:
                try_show = Show.objects.get(title=postData['title_txt'])
            except Show.DoesNotExist:
                try_show = None
            if try_show != None:
                errors["title"] = "The title " + postData['title_txt'] + " already exists."
        if len(postData['network_txt']) < 3:
            errors["network"] = "Network should be at least 3 characters long"
        if len(postData['desc_txt']) > 0 and len(postData['desc_txt']) < 10:
            errors["desc"] = "Movie description should be at least 10 characters if provided"
        if postData["release_txt"] == "":
              errors["release_date"] = "Choose a release date."
        elif datetime.strptime(postData["release_txt"], '%Y-%m-%d') > datetime.now():
              errors["release_date"] = "The date you have chosen is in the future."
        return errors

class Show (models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

