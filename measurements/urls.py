from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_measurements, name='measurementsList'),
    path('gett/<int:pPk>/', views.get_one_measurement, name='getOneMeasurements'),
    path('del/<int:pPk>/', views.delete_one_measurement, name='deleteOneMeasurements'),
    path('up/<int:pPk>/val&<int:val>/unit&<slug:un>/place&<slug:pl>', views.update_one_measurement, name='updateOneMeasurements')
]