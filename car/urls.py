from django.conf.urls import url
from .views import carpreview, news, carcomplete
from django.conf import settings
from django.conf.urls.static import static
urlpatterns =[
    url("cars", carpreview, name="car preview"),
    url("news", news, name="news list"),
    url("car", carcomplete, name="car complete")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
