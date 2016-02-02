#coding=utf8
from rest_framework import serializers #@UnresolvedImport
from models import Service_category, Service_type,\
    Service_provider, Service_protocol, Service_status, Service_tag,\
    Service_base, Service_fieldType, Service_reqField, Service_respField,\
    Service_reqDemo, Service_respDemo, Service_api, Service_errorType,\
    Service_errorCode, Service_upgrade, Service_statistics, Service_contact,\
    Service_others, Service_invokeDemo, Common_httpDemo, Service_price,\
    Service_activePack, Service_sdkPack
    
class ServiceCategorySerializer(serializers.HyperlinkedModelSerializer):
#    def to_representation(self, obj):
#        return { 'category_name': obj.category_name, }
    class Meta:
        model = Service_category 
        fields = ('url','id','category_name','parent_category_id','serve_cate_logo','cate_type',
                  'create_time','modify_time','order_num',)


class ServiceTypeSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.PrimaryKeyRelatedField(read_only=True);
    class Meta:
        model = Service_type
        fields = ('url','id','category','type_name','parent_type_id','serve_type_logo','type_base',
                  'create_time','modify_time','order_num',)


class ServiceProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service_provider
        fileds = ('url','id','provider_name','base_provider','create_time','modify_time',)
        

class ServiceProtocolSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Service_protocol 
         

class ServiceStatusSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Service_status
        

class ServiceTagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service_tag
        fields = ('url','id','tag_name','tag_color','create_time','modify_time','base_tags')


class ServiceBaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service_base
        fields = ('url','id','serve_name','serve_desc','status','serve_tags','provider',
                  'protocol','serve_type','serve_logo','base_statistics','base_activepack','base_sdkpack','base_price',
                  'create_time','modify_time')
        
        
class ServiceFieldTypeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Service_fieldType
        

class ServiceReqFieldSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    service = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Service_reqField
        

class ServiceRespFieldSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    service = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Service_respField
        

class ServiceReqDemoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    service = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Service_reqDemo
        

class ServiceRespDemoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    service = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Service_respDemo
        

class ServiceApiSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    service = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Service_api
        fields = ["id","service","format","create_time","modify_time","proxy_url"]


class ServiceApiSecretSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
#    service = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Service_api
        fields = ["id","service","format","create_time","modify_time","serve_url","proxy_url"]
           

class ServiceErrorTypeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    service = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Service_errorType
        

class ServiceErrorCodeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    service = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Service_errorCode
        

class ServiceUpgradeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    service = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Service_upgrade
        

class ServiceStatisticsSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Service_statistics
        

class ServiceContactSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    service = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Service_contact
        

class ServiceOthersSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    service = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Service_others
        

class ServiceInvokeDemoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    service = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Service_invokeDemo
        

class CommonHttpDemoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Common_httpDemo
        

class ServicePriceSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    service = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Service_price
        

class ServiceActivePackSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    service = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Service_activePack


class ServiceSdkPackSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    service = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Service_sdkPack


class Base_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    serve_name = serializers.CharField(max_length=200)
    class Meta:
        model = Service_base
        fields = ('id','serve_name')
        
class Type_Base_Serializer(serializers.ModelSerializer):
    serve_bases = Base_Serializer(required=False,many=True)
    class Meta:
        model = Service_type
        fields = ('id','type_name','serve_bases')
    
class Cate_Type_Base_Serializer(serializers.ModelSerializer):
#    id = serializers.IntegerField()
#    category_name = serializers.CharField(max_length=200)
#    serve_cate_logo = serializers.ModelField(model_field=Service_category()._meta.get_field('serve_cate_logo'))
    serve_types = Type_Base_Serializer(required=False,many=True)
    class Meta:
        model = Service_category
        fields = ('id','category_name','serve_cate_logo','serve_types')
    
#class UserSerializer(serializers.ModelSerializer):
#    categorys = serializers.PrimaryKeyRelatedField(many=True, queryset=Service_category.objects.all()) #@UndefinedVariable
#    class Meta:
#        model = User
#        fields = ('id', 'username', 'categorys')

