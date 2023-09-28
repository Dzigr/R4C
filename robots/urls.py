from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import CreateRobotView

urlpatterns = [
    path('add/', csrf_exempt(CreateRobotView.as_view()), name='add_robot'),
]
