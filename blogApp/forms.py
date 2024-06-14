from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div
from blogApp.models import Offer

class OfferForm(ModelForm):
    class Meta:
        model = Offer
        fields = ['type','category','title',
                  'summary',
                  'description',
                  'city',
                  'min_age',
                  'max_age',
                  'gender']
        labels = {
            'type': "Type d'annonce",
            'category': 'Catégorie',
            'title': "Titre de l'annonce",
            'summary': 'Résumé',
            'city': 'Ville',
            'min_age': 'Âge apparent minimal',
            'max_age': 'Âge apparent maximal',
            'gender': 'Genre'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('type', css_class='w-full'),
                Div('category', css_class='w-full'),
                css_class='flex gap-2 w-full'),
            Fieldset(
                '',
                'title',
                'summary',
                'description',
                'city',
            ),
            Div(
                Div('min_age'),
                Div('max_age'),
                Div('gender'),
                css_class='grid grid-cols-2 md:grid-cols-3 gap-2'
            )
        )
        self.helper.form_id = 'id-offerForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Déposer mon annonce'))



