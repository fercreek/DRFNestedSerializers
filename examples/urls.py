from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from contacts.views import ContractorView, ContactView, GroupView
from .views import RecipeView, IngredientView

router = DefaultRouter()
router.register(r'recipientes', RecipeView)
router.register(r'ingredientes', IngredientView)
router.register(r'contratantes', ContractorView)
router.register(r'contactos', ContactView)
router.register(r'grupos', GroupView)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
