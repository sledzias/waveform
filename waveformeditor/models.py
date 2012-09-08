from django.db import models
from django.contrib.auth.models import User

class Circuit(models.Model):
    """
    Model dokumentu przechowujacego schemat ukladu logicznego
    """
    created_by = models.ForeignKey(User, related_name='+', editable=False)
    data = models.TextField()
    title = models.CharField(max_length=100)

    pub_date = models.DateTimeField('date published',auto_now_add=True, editable=False)
    edit_date = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return self.title
    def __repr__(self):
        return self.data