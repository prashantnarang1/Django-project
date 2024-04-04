from django.contrib import admin
from django.urls import path,include
from gundepot import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home),
    path('about',views.about),
    path('product_details/<pid>',views.product_details),
    path('viewcart',views.viewcart),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('addtocart/<pid>',views.addtocart),
    path('remove/<cid>',views.remove),
    path('updateqty/<qv>/<cid>',views.updateqty),
    path('placeorder',views.placeorder),
    path('catfilter/<cv>',views.catfilter),
    path('sort/<abc>',views.sort),
    path('range',views.range),
    path('makepayment',views.makepayment),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

