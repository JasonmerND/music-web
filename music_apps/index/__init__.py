import os
from django.apps import AppConfig

# 修改App在后台显示的名称
default_app_config = 'index.IndexConfig'

# 获取当前App的名称
def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


class IndexConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = '网站首页'

