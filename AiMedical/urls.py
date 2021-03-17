from django.contrib import admin
from django.urls import path
from AiApp import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',views.home,name='home'),
    url('resulttumor/',views.resulttumor,name='resulttumor'),
    url('resultpnu/',views.resultpnu,name='resultpnu'),
    url('resulttb/',views.resulttb,name='resulttb'),
    url('resultbreast/',views.resultbreast,name='resultbreast'),
    url('brainForm/',views.brainForm,name='brainForm'),
    url('tbForm/',views.tbForm,name='tbForm'),
    url('pueForm/',views.pueForm,name='pueForm'),
    url('breastForm/',views.breastForm,name='breastForm'),


]
urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
