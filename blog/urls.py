from django.urls import path
from .  import views
from django.conf.urls.static import static
from AR import settings
from django.conf.urls import url 

urlpatterns = [
    path('', views.index, name="index" ),
    path('boutique', views.boutique, name="boutique" ),
    path('produits-detail/<slug>/',views.details, name='details'),
    #path('detailsnew/<str:detailsnew_id>/  views.detailsnew'),
    url(r'^detailsnew/(?P<detailsnew_id>[0-9]+)$', views.detailsnew, name='detailsnew'),    url(r'^rechercheform/$',views.rechercheform,name='rechercheform'),
    path('account/login/', views.loginPage, name='loginPage'),
    path('account/logout/', views.logoutUser, name='logout'),
    path('account/register/', views.register, name='registerPage'),
    path('account/ajoutimmo/', views.ajoutimmoPage, name='ajoutimmoPage'),
    path('account/logout/', views.logoutUser, name='logout'),
    url(r'^account/passwordchange/$',views.passwordchange,name='passwordchange'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

