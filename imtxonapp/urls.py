from django.urls import path

from imtxonapp import views, admin
from .views import murojat,yuborish


urlpatterns = [
    path('', views.index, name='index'),
    path('murojat', murojat, name='murojat'),
    path('yuborish', yuborish, name='yuborish')
]
