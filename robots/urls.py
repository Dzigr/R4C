from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import CreateRobotView, DownloadExcelView

urlpatterns = [
    path('add/', csrf_exempt(CreateRobotView.as_view()), name='add_robot'),
    path('get_stat/', csrf_exempt(DownloadExcelView.as_view()), name='get_excel_data'),
]
