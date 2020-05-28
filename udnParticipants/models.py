from enum import Enum

from django.db import models
from django.http import HttpResponseRedirect


class Participant(models.Model):
    """ The Participant Model """
    class ReviewStatus(Enum):
        notReviewed = ('NR', 'Not Reviewed')
        reviewedAccepted = ('RA', 'Reviewed - Accepted')
        notAccepted = ('RNA', 'Reviewed - Not Accepted')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    fullname = models.CharField(help_text='Enter your full name', max_length=100)
    age = models.IntegerField(help_text='Enter your age')
    siblings = models.BooleanField(help_text='Click on the checkbox if you have siblings', default=False)
    environmentExposures = models.TextField()
    geneticMutations = models.TextField()
    reviewItem = models.CharField(choices=[x.value for x in ReviewStatus], editable=True, default='Not Reviewed', max_length=20)
    createdAt = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """Return URL of the object's list view."""
        return HttpResponseRedirect("/login")

