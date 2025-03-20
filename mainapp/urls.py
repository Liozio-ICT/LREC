from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('the-agnes', views.agnes, name="the_agnes"),
    path('the-agnes/primrose', views.primrose, name="primrose"),
    path('the-agnes/ivy', views.ivy, name="ivy"),
    path('the-agnes/emerald', views.emerald, name="emerald"),
    path('the-agnes/temp', views.temp, name="temp"),
    path('the-agnes/aurora', views.aurora, name="aurora"),
]
