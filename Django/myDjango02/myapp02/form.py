from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# DB에서 가져와서 폼 인증하기
class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ("username", "email")