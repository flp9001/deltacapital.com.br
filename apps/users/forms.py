from django.contrib import auth
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class UserChangeFormSuper(auth.forms.UserChangeForm):
    class Meta(auth.forms.UserChangeForm.Meta):
        model = User


class UserChangeFormOwner(UserChangeFormSuper):
    def __init__(self, *args, **kwargs):
        super(UserChangeFormSuper, self).__init__(*args, **kwargs)
        self.fields["user_type"].choices = self.fields["user_type"]._choices[1:]

    def validate(self):
        return False


class UserCreationForm(auth.forms.UserCreationForm):

    error_message = auth.forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(auth.forms.UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])
