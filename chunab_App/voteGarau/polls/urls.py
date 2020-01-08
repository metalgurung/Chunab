from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'), #int:question_id as question_id is passed as parameters for detail function
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('resultsdata/<str:obj>/', views.resultsData, name="resultsdata"),
    # even tohugh its inapporpaite isneeded to pass jsondata
]