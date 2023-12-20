from django.urls import include, path


urlpatterns = [
    path("ssi/", include("ssi_views.urls")),
    path("", include("app.urls")),
]
