from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class LoginForm(AuthenticationForm):

    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        label = {
            'email': 'Email',
            'password': 'Mot de passe'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('email', css_class='w-full'),
                Div('password', css_class='w-full'),
                css_class='flex gap-2 w-full'),
        )
        self.helper.form_id = 'id-loginForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Se connecter'))



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)