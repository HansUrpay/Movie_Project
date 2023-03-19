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
    path('swagger/', schema_view.with_ui("swagger", cache_timeout=0), name="swagger-docs"),
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/movie/', include("movies.urls")),
    path("api/v1/user/", include("user.urls")),
    path("api/v1/rent/", include("rent.urls")),
]
