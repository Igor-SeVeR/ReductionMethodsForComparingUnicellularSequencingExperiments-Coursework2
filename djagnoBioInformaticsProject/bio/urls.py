from django.urls import path

from .views import MainView

app_name = "bio"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('get_mtx_data', MainView.as_view()),
]
