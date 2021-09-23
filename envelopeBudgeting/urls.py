from django.urls import path

from . import views

app_name = 'envelopeBudgeting'
urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('<int:env_id>/', views.envelopes, name='envelopes'),
    path('newenvelope/', views.addEnvelope, name='newenvelope'),
    path('deleteenvelope/', views.deleteEnvelope, name='deleteenvelope'),
    path('<int:env_id>/newtransaction/', views.addTransaction, name='newtransaction'),
    path('<int:env_id>/deletetransaction/', views.deleteTransaction, name='deletetransaction'),
    path('<int:env_id>/updateenvelope/', views.updateEnvelope, name='updateenvelope'),
]