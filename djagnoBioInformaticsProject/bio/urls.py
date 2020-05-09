from django.urls import path

from .views import UseBuiltModel, BuildModel

app_name = "bio"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('get_mtx_data', UseBuiltModel.as_view()),
    path('build_model_and_get_mtx_data', BuildModel.as_view())
]
