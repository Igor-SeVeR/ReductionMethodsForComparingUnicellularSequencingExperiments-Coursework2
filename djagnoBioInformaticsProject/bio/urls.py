from django.urls import path

from .views import MainView, MainView2

app_name = "bio"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('get_mtx_data', MainView.as_view()),
    path('build_model_and_get_mtx_data', MainView2.as_view())
]
