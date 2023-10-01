from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import OrderRobotView

urlpatterns = [
    path("robot/", csrf_exempt(OrderRobotView.as_view()), name="order_robot")
]
