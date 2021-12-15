from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationView(ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'image', 'message']