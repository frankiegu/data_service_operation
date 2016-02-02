#coding=utf8
from django.conf.urls import url, include

from service import views #@UnresolvedImport
from rest_framework import routers #@UnresolvedImport

router = routers.DefaultRouter()
router.register(r'category', views.ServiceCategoryViewSet)
router.register(r'type', views.ServiceTypeViewSet)
router.register(r'provider', views.ServiceProviderViewSet)
router.register(r'protocol', views.ServiceProtocolViewSet)
router.register(r'status', views.ServiceStatusViewSet)
router.register(r'tag', views.ServiceTagViewSet)
router.register(r'base', views.ServiceBaseViewSet)
router.register(r'filedtype', views.ServiceFieldTypeViewSet)
router.register(r'reqfield', views.ServiceReqFieldViewSet)
router.register(r'respfield', views.ServiceRespFieldViewSet)
router.register(r'reqdemo', views.ServiceReqDemoViewSet)
router.register(r'respdemo', views.ServiceRespDemoViewSet)
router.register(r'api', views.ServiceApiViewSet,'api')
router.register(r'api_secret', views.ServiceApiSecretViewSet,'api_secret')
router.register(r'errortype', views.ServiceErrorTypeViewSet)
router.register(r'errorcode', views.ServiceErrorCodeViewSet)
router.register(r'upgrade', views.ServiceUpgradeViewSet)
router.register(r'statistics', views.ServiceStatisticsViewSet)
router.register(r'contact', views.ServiceContactViewSet)
router.register(r'others', views.ServiceOthersViewSet)
router.register(r'invokedemo', views.ServiceInvokeDemoViewSet)
router.register(r'httpdemo', views.CommonHttpDemoViewSet)
router.register(r'price', views.ServicePriceViewSet)
router.register(r'activepack', views.ServiceActivePackViewSet)
router.register(r'sdkpack', views.ServiceSdkPackViewSet)
router.register(r'cate_type_base', views.Cate_Type_Base_ViewSet, 'cate_type_base')

urlpatterns = [
    url(r'^rest/service/', include(router.urls), name='model-detail'),
]
