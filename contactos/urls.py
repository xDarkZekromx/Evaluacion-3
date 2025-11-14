from django.urls import path,include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"contactos", views.ContactoViewSet)

urlpatterns = [
    # Rutas JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('personas/', views.lista_contactos, name='lista_contactos'),                   # Pagina de Contactos
    path('personas/nuevo/', views.nuevo_contacto, name='nuevo_contacto'),               # Pagina para agregar nuevo contacto
    path('personas/<int:pk>/', views.detalle_contacto, name='detalle_contacto'),        # Pagina de detalle de contacto
    path('personas/<int:pk>/editar/', views.editar_contacto, name='editar_contacto'),   # Pagina para editar contacto
    path('personas/<int:pk>/eliminar/', views.eliminar_contacto, name='eliminar_contacto'),     # Pagina para eliminar contacto


]