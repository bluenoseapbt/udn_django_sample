from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from udnParticipants.models import Participant


class ParticipantForm(forms.ModelForm):
    """ ModelForm for the Participant model"""
    class Meta:
        model = Participant
        fields = ('fullname', 'age', 'siblings', 'environmentExposures', 'geneticMutations')

    def __init__(self, *args, **kwargs):
            """Initiate form with Crispy Form's FormHelper"""
            super(ParticipantForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.fields['environmentExposures'].widget.attrs['rows'] = 4
            self.fields['environmentExposures'].widget.attrs['columns'] = 15
            self.fields['environmentExposures'].label = 'Environment Exposures'
            self.fields['geneticMutations'].widget.attrs['rows'] = 4
            self.fields['geneticMutations'].widget.attrs['columns'] = 15
            self.fields['geneticMutations'].label = 'Genetic Mutations'
            self.helper.add_input(Submit('submit', 'Submit'))
            self.helper.add_input(Submit(
                'cancel',
                'Cancel',
                css_class='btn-danger',
                formnovalidate='formnovalidate',
                )
            )

