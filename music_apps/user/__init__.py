import os
from django.apps import AppConfig

# 修改App在后台显示的名称
default_app_config = 'user.UserConfig'

# 获取当前App的名称
def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


class UserConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = '用户管理'

