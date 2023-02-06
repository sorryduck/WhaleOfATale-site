from django.urls import path
from .views import *


urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('categories/<slug:cat_slug>/', CategoryView.as_view(), name='showByCats'),
    path('feedback/', FeedbackFormView.as_view(), name='feedback'),
    path('about/', about, name='about'),
    path('ocean_news/', NewsView.as_view(), name='ocean_news'),
    path('search/', SearchView.as_view(), name='search'),
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
