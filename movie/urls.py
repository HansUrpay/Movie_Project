from django.contrib import admin
from django.urls import path, include

# para documentacion de la API
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
    title="Movie API",
    default_version="v1",
    description="API para recordar Django",
    terms_of_service= "https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="hansurpayh@gmail.com"),
    license=openapi.License(name="MIT")
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('/', schema_view.with_ui("/", cache_timeout=0), name="swagger-docs"),
    # path('swagger/', schema_view.with_ui("swagger", cache_timeout=0), name="swagger-docs"),
    path('admin/', admin.site.urls),
    path('movie/', include("movies.urls")),
    path("user/", include("user.urls")),
    path("rent/", include("rent.urls")),
]
