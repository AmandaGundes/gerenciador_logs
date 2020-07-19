from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from .views.log_views import *
from .views.usuario_views import *
from .views import restframewok_views

router = routers.DefaultRouter()
router.register(r'logs', restframewok_views.LogApiViewSet)

urlpatterns = [
    path('listar_logs/', listar_logs, name='listar_logs'),
    path('detalhar_log/<int:id>', detalhar_log, name='detalhar_log'),
    path('cadastrar_logs/', cadastrar_log, name='cadastrar_log'),
    path('editar_log/<int:id>', editar_log, name='editar_log'),
    path('remover_log/<int:id>', remover_log, name='remover_log'),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('logar_usuario/', logar_usuario, name='logar_usuario'),
    path('deslogar_usuario/', deslogar_usuario, name='deslogar_usuario'),
    path('', include(router.urls)),
    path('get_token', obtain_auth_token),
]
