from django.urls import path

from waitlist import views


app_name = 'waitlist'

urlpatterns = [
    path('create/', views.CreateWaitListView.create('self', 'request'), name='create'),
]
