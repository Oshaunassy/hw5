from django.urls import path
from users import views


urlpatterns = [
    path('registration/', views.registration_api_view),
    path('authorazation/', views.authorization_api_view)
]