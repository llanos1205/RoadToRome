from . import views
from django.urls import include, re_path


urlpatterns = [
     re_path('wall/',views.WallView.as_view())
 ]
 