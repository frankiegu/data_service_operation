#coding=utf8
from django.db import models
from django.utils import timezone
from DataOperation import settings #@UnresolvedImport
#from pygments.formatters.html import HtmlFormatter #@UnresolvedImport
#from pygments import highlight #@UnresolvedImport
#from pygments.lexers import get_lexer_by_name #@UnresolvedImport
#from pygments.lexers import get_all_lexers #@UnresolvedImport
#from pygments.styles import get_all_styles #@UnresolvedImport
#from django.contrib.auth.models import User

#LEXERS = [item for item in get_all_lexers() if item[1]]
#LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
#STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Service_category(models.Model):
    category_name = models.CharField(max_length=100)
    cate_abbreviation = models.SlugField(max_length=100,unique=True)
    parent_category_id = models.IntegerField(blank=True,default=0)
    serve_cate_logo = models.ImageField(upload_to='images/ico/',blank=True)
    create_time = models.DateField(blank=True,default=timezone.now)
    modify_time = models.DateField(blank=True,default=timezone.now)
    order_num = models.IntegerField()
#    owner = models.ForeignKey(User, related_name='categorys')
#    highlighted = models.TextField()
    def __unicode__(self):
        return self.category_name
#    def save(self, *args, **kwargs):
#        lexer = get_lexer_by_name(self.category_name)
#        linenos = self.serve_cate_logo and 'table' or False
#        options = self.order_num and {'order_num': self.title} or {}
#        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
#        self.highlighted = highlight(self.code, lexer, formatter)
#        super(Service_category, self).save(*args, **kwargs)
    class Meta:
        ordering = ['order_num']
        verbose_name = u"服务类别"
        verbose_name_plural = verbose_name


class Service_type(models.Model):
    category = models.ForeignKey(Service_category, related_name='cate_type')
    type_name = models.CharField(max_length=100)
    type_abbreviation = models.SlugField(max_length=100,unique=True)
    parent_type_id = models.IntegerField(blank=True,default=0)
    serve_type_logo = models.ImageField(upload_to='images/ico/',blank=True)
    create_time = models.DateField(blank=True,default=timezone.now)
    modify_time = models.DateField(blank=True,default=timezone.now)
    order_num = models.IntegerField()
    def __unicode__(self):
        return self.type_name
    class Meta:
        ordering = ['order_num']
        verbose_name = u"服务类型"
        verbose_name_plural = verbose_name


class Service_provider(models.Model):
    provider_name = models.CharField(max_length=200)
    create_time = models.DateTimeField(blank=True,default=timezone.now)
    modify_time = models.DateTimeField(blank=True,default=timezone.now)
    def __unicode__(self):
        return self.provider_name
    class Meta:
        verbose_name = u"数据供应商"
        verbose_name_plural = verbose_name
        
        
class Service_protocol(models.Model):
    protocol_name = models.CharField(max_length=200)
    support_method = models.CharField(max_length=200,blank=True) #如Http，则对应get,post,put,delete,patch等
    create_time = models.DateTimeField(blank=True,default=timezone.now)
    modify_time = models.DateTimeField(blank=True,default=timezone.now)
    def __unicode__(self):
        return self.protocol_name
    class Meta:
        verbose_name = u"服务协议"
        verbose_name_plural = verbose_name
        
        
class Service_status(models.Model):
    status_name = models.CharField(max_length=200)
    create_time = models.DateTimeField(blank=True,default=timezone.now)
    modify_time = models.DateTimeField(blank=True,default=timezone.now)
    def __unicode__(self):
        return self.status_name
    class Meta:
        verbose_name = u"服务状态"
        verbose_name_plural = verbose_name
        
        
class Service_tag(models.Model):
    tag_name = models.CharField(max_length='100');
    tag_color = models.IntegerField();
    create_time = models.DateTimeField(blank=True,default=timezone.now)
    modify_time = models.DateTimeField(blank=True,default=timezone.now)
    def __unicode__(self):
        return self.tag_name
    class Meta:
        verbose_name = u"服务标签"
        verbose_name_plural = verbose_name
    
    
class Service_base(models.Model):
    serve_name = models.CharField(max_length=200)
    serve_abbreviation = models.SlugField(max_length=100,unique=True)
    serve_desc = models.TextField()
    status = models.ForeignKey(Service_status)
    serve_tags = models.ManyToManyField(Service_tag, related_name='base_tags' ,blank=True)
    provider = models.ForeignKey(Service_provider, related_name='base_provider')
    protocol = models.ForeignKey(Service_protocol)
    serve_type = models.ForeignKey(Service_type, related_name='type_base')
    serve_logo = models.ImageField(upload_to='images/service/ico/',blank=True)
    create_time = models.DateTimeField(blank=True,default=timezone.now)
    modify_time = models.DateTimeField(blank=True,default=timezone.now)
    def __unicode__(self):
        return self.serve_name
    class Meta:
        verbose_name = u"服务基础信息"
        verbose_name_plural = verbose_name


class Service_fieldType(models.Model):
    field_type_name = models.CharField(max_length=200)
    create_time = models.DateField(blank=True,default=timezone.now)
    modify_time = models.DateField(blank=True,default=timezone.now)
    def __unicode__(self):
        return self.field_type_name
    class Meta:
        verbose_name = u"服务参数类型"
        verbose_name_plural = verbose_name


REQUIRED_CHIOCES = (
                (0, '否'),(1, '是'),
        )
class Service_reqField(models.Model):
    service =  models.ForeignKey(Service_base,related_name="base_reqfield")
    field_name = models.CharField(max_length=100)
    field_type = models.ForeignKey(Service_fieldType)
    required = models.IntegerField(choices=REQUIRED_CHIOCES)
    description = models.CharField(max_length=1000)
    create_time = models.DateTimeField(blank=True,default=timezone.now)
    modify_time = models.DateTimeField(blank=True,default=timezone.now)
    def __unicode__(self):
        return self.service.serve_name
    class Meta:
        verbose_name = u"服务传参设置"
        verbose_name_plural = verbose_name


class Service_respField(models.Model):
    service =  models.ForeignKey(Service_base,related_name="base_respfield")
    field_name = models.CharField(max_length=100)
    field_type = models.ForeignKey(Service_fieldType)
    description = models.CharField(max_length=1000)
    create_time = models.DateTimeField(blank=True,default=timezone.now)
    modify_time = models.DateTimeField(blank=True,default=timezone.now)
    def __unicode__(self):
        return self.service.serve_name
    class Meta:
        verbose_name = u"服务返回值设置"
        verbose_name_plural = verbose_name


class Service_reqDemo(models.Model):
    service =  models.ForeignKey(Service_base,related_name="base_reqdemo")
    demo_format = models.CharField(max_length=100)
    demo_str = models.TextField(max_length=2000)
    create_time = models.DateTimeField(blank=True,default=timezone.now)
    modify_time = models.DateTimeField(blank=True,default=timezone.now)
    def __unicode__(self):
        return self.service.serve_name
    class Meta:
        verbose_name = u"服务请求示例"
        verbose_name_plural = verbose_name
    
    
class Service_respDemo(models.Model):
    service =  models.ForeignKey(Service_base,related_name="base_respdemo")
    demo_format = models.CharField(max_length=100)
    demo_str = models.TextField(max_length=2000)
    create_time = models.DateTimeField(blank=True,default=timezone.now)
    modify_time = models.DateTimeField(blank=True,default=timezone.now)
    def __unicode__(self):
        return self.service.serve_name
    class Meta:
        verbose_name = u"服务返回示例"
        verbose_name_plural = verbose_name


class Service_api(models.Model):
    service = models.OneToOneField(Service_base,related_name="base_api")
    format = models.CharField(max_length=100)
    create_time = models.DateTimeField(blank=True,default=timezone.now)
    modify_time = models.DateTimeField(blank=True,default=timezone.now)
    serve_url = models.CharField(max_length=500)
    def _get_proxy_url(self):
        return settings.PROXY_SERVICE_URL + self.service.serve_type.category.cate_abbreviation+"/"\
        + self.service.serve_type.type_abbreviation+"/"\
        + self.service.serve_abbreviation+"/"
    proxy_url = property(_get_proxy_url)  #models.CharField(max_length=500)
    def __unicode__(self):
        return self.service.serve_name
    class Meta:
        verbose_name = u"服务api详情"
        verbose_name_plural = verbose_name


class Service_errorType(models.Model):
    error_type_name = models.CharField(max_length=200)
    create_time = models.DateField(blank=True,default=timezone.now)
    modify_time = models.DateField(blank=True,default=timezone.now)
    def __unicode__(self):
        return self.error_type_name
    class Meta:
        verbose_name = u"调用错误类型"
        verbose_name_plural = verbose_name

class Service_errorCode(models.Model):
    service = models.ForeignKey(Service_base)
    error_type = models.ForeignKey(Service_errorType, related_name="errorType_errorCode")
    error_code = models.CharField(max_length=100)
    error_name = models.CharField(max_length=1000)
    create_time = models.DateField(blank=True,default=timezone.now)
    modify_time = models.DateField(blank=True,default=timezone.now)
    def __unicode__(self):
        return  self.service.serve_name+self.error_name #逗号表示字符串连接，中间自动添加空格
    class Meta:
        verbose_name = u"调用错误代码"
        verbose_name_plural = verbose_name
    
    
class Service_upgrade(models.Model):
    service = models.ForeignKey(Service_base,related_name="base_upgrade")
    upgrade_title = models.CharField(max_length=100)
    upgrade_contents = models.CharField(max_length=1000)
    upgrade_time = models.DateTimeField(blank=True,default=timezone.now)
    create_time = models.DateField(blank=True,default=timezone.now)
    modify_time = models.DateField(blank=True,default=timezone.now)
    def __unicode__(self):
        return self.service.serve_name
    class Meta:
        verbose_name = u"服务更新记录"
        verbose_name_plural = verbose_name


class Service_statistics(models.Model):
    service = models.OneToOneField(Service_base,related_name="base_statistics")
    scores = models.DecimalField(max_digits=2, decimal_places=1)
    app_counts = models.IntegerField()
    invoke_counts = models.IntegerField()
    scan_counts = models.IntegerField()
    create_time = models.DateField(blank=True,default=timezone.now)
    modify_time = models.DateField(blank=True,default=timezone.now)
    def __unicode__(self):
        return self.service.serve_name
    class Meta:
        verbose_name = u"服务积分和统计"
        verbose_name_plural = verbose_name


class Service_contact(models.Model):
    service = models.OneToOneField(Service_base)
    support_team = models.CharField(max_length=500)
    support_telno = models.CharField(max_length=20)
    groupQQ = models.CharField(max_length=20)
    contactQQ = models.CharField(max_length=100)
    partnerQQ = models.CharField(max_length=100)
    create_time = models.DateField(blank=True,default=timezone.now)
    modify_time = models.DateField(blank=True,default=timezone.now)
    def __unicode__(self):
        return self.service.serve_name
    class Meta:
        verbose_name = u"服务联络信息"
        verbose_name_plural = verbose_name


class Service_others(models.Model):
    service = models.ForeignKey(Service_base)
    content = models.CharField(max_length=100)
    detail = models.TextField(max_length=1000)
    create_time = models.DateField(blank=True,default=timezone.now)
    modify_time = models.DateField(blank=True,default=timezone.now)
    def __unicode__(self):
        return self.service.serve_name
    class Meta:
        verbose_name = u"其他服务相关"
        verbose_name_plural = verbose_name


class Service_invokeDemo(models.Model):
    service = models.ForeignKey(Service_base)
    language = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    hyperlink = models.CharField(max_length=500)
    provider = models.CharField(max_length=200)
    create_time = models.DateField(blank=True,default=timezone.now)
    modify_time = models.DateField(blank=True,default=timezone.now)
    def __unicode__(self):
        return self.language + "," + self.title
    class Meta:
        verbose_name = u"服务调用示例"
        verbose_name_plural = verbose_name
    

class Common_httpDemo(models.Model):
    language = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    hyperlink = models.CharField(max_length=500)
    create_time = models.DateField(blank=True,default=timezone.now)
    modify_time = models.DateField(blank=True,default=timezone.now)
    def __unicode__(self):
        return self.language + self.title
    class Meta:
        verbose_name = u"Http通用示例"
        verbose_name_plural = verbose_name


PER_UNIT_CHIOCES = (
                (0, '每天'),(1, '每周'),(3, '每月'),(4, '每年'),(2, '从不')
        )
class Service_price(models.Model):
    service = models.OneToOneField(Service_base,related_name="base_price")
    is_free = models.BooleanField(default=True)
    free_times_per = models.IntegerField()
    per_unit = models.IntegerField(choices=PER_UNIT_CHIOCES)
    cost = models.DecimalField(max_digits=5, decimal_places=0)
    create_time = models.DateField(blank=True,default=timezone.now)
    modify_time = models.DateField(blank=True,default=timezone.now)
    def __unicode__(self):
        return self.service.serve_name
    class Meta:
        verbose_name = u"服务定价"
        verbose_name_plural = verbose_name


ACTIVE_PACK_STATUS_CHIOCES = (
                (0, '失效'),(1, '生效')
        )

ACTIVE_PACK_COST_BY = (
                (0, '包次'),(1, '包时')
        )

TIME_UNIT_CHIOCES = (
                (0, '每天'),(1, '每周'),(3, '每月'),(4, '每年'),(2, '从不')
        )
class Service_activePack(models.Model):
    service = models.ForeignKey(Service_base,related_name="base_activepack")
    pack_name = models.CharField(max_length=100)
    pack_desc = models.CharField(max_length=500)
    pack_price = models.DecimalField(max_digits=6, decimal_places=2)
    by_counts_or_time = models.IntegerField(choices=ACTIVE_PACK_COST_BY)
    pack_counts = models.IntegerField()
    pack_effective_time = models.PositiveIntegerField()
    time_unit = models.IntegerField(choices=TIME_UNIT_CHIOCES)
    status = models.IntegerField(choices=ACTIVE_PACK_STATUS_CHIOCES)
    create_time = models.DateField(blank=True,default=timezone.now)
    modify_time = models.DateField(blank=True,default=timezone.now)
    def __unicode__(self):
        return self.service.serve_name
    class Meta:
        verbose_name = u"服务活动套餐"
        verbose_name_plural = verbose_name
    
    
class Service_sdkPack(models.Model):
    service = models.OneToOneField(Service_base,related_name="base_sdkpack")
    pack_name = models.CharField(max_length=100)
    pack_desc = models.CharField(max_length=500)
    free_times_per = models.IntegerField()
    per_unit = models.IntegerField(choices=PER_UNIT_CHIOCES)
    single_client_free_times_per =  models.IntegerField()
    single_client_per_unit = models.IntegerField(choices=PER_UNIT_CHIOCES)
    create_time = models.DateField(blank=True,default=timezone.now)
    modify_time = models.DateField(blank=True,default=timezone.now)
    def __unicode__(self):
        return self.service.serve_name + self.pack_name
    class Meta:
        verbose_name = u"SDK使用优惠"
        verbose_name_plural = verbose_name
        
        
