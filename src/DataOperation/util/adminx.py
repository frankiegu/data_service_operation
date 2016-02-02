#coding=utf8
import xadmin
from xadmin import views
#from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
#from xadmin.plugins.inline import Inline
#from xadmin.plugins.batch import BatchChangeAction

class MainDashboard(object):
    widgets = [
#        [
#            {"type": "html", "title": "Test Widget", "content": "<h3> Welcome to Xadmin! </h3><p>Join Online Group: <br/>QQ Qun : 568901700</p>"},
#            {"type": "chart", "model": "app.accessrecord", 'chart': 'user_count', 'params': {'_p_date__gte': '2015-01-01', 'p': 1, '_p_date__lt': '2015-12-30'}},
#            {"type": "list", "model": "app.host", 'params': {
#                'o':'-guarantee_date'}},
#        ],
#        [
#            {"type": "qbutton", "title": "Quick Start", "btns": [{'model': Service_base}, {'model':Service_price}, {'title': "Google", 'url': "http://www.google.com"}]},
#            {"type": "addform", "model": Service_activePack},
#        ]
    ]
xadmin.site.register(views.website.IndexView, MainDashboard)


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSetting(object):
#    global_search_models = [Service_base, Service_price]
    #图标样式类型保存在font-awesome.css中
    global_models_icon = {
#        Service_base: 'fa fa-laptop', 
#        Service_price: 'fa fa-desktop',
    }
    site_title = '数据服务运营平台'
    site_footer  = '数据服务运营平台  - 版权所有:神州数码信息系统有限公司'
    menu_style = 'default' #'accordion'
xadmin.site.register(views.CommAdminView, GlobalSetting)
