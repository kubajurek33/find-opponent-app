from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from users.forms import CustomLoginForm


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('signup', views.signup, name="signup"),
    path('login/', LoginView.as_view(
        authentication_form=CustomLoginForm),
         name="login"
         ),
    path('editprofile', views.editprofile, name="editprofile"),
    path('addevent', views.addevent, name="addevent"),
    path('editevent/<id>', views.editevent, name="editevent"),
    path('showevents', views.showevents, name="showevents"),
    path('ownevents', views.ownevents, name="ownevents"),
    path('profile/<id>', views.get_user_profile, name='profile'),
    path('delete/<id>', views.deleteevent, name='deleteevent'),
]
