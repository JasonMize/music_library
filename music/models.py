from django.db import models
from django.core.urlresolvers import reverse



class Artist (models.Model):

    name = models.CharField(max_length = 40)

    wiki_url = models.URLField(max_length=200)
    
 



    def get_absolute_url(self):
        return reverse ("music:music", kwargs={"id":self.pk})





