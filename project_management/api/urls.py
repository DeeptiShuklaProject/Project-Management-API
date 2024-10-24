from django.urls import path
from .views import home  # Import your views here

urlpatterns = [
    path('', home, name='api_home'),  # You can set up a home view or any other view
    # Add any additional API routes here
]
