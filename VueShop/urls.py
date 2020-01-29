"""VueShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path, include, path
import xadmin
from django.views.generic import TemplateView
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from goods.views import GoodsListViewSet, CategoryViewset, BannerViewset, IndexCategoryViewset
from trade.views import ShoppingCartViewset, OrderViewset, AlipayView
from .settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from users.views import SmsCodeViewset
from users.views import UserViewset
from user_operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset

router = DefaultRouter()

# 配置goods的url
router.register(r'goods', GoodsListViewSet, basename='goods')

# 配置category的url
router.register(r'categorys', CategoryViewset, basename='categorys')

router.register(r'code', SmsCodeViewset, basename='code')

router.register(r'users', UserViewset, basename='users')

# 收藏
router.register(r'userfavs', UserFavViewset, basename='userfavs')

# 留言
router.register(r'messages', LeavingMessageViewset, basename='messages')

# 收货地址
router.register(r'address', AddressViewset, basename='address')

# 购物车url
router.register(r'shopcarts', ShoppingCartViewset, basename='shopcarts')

# 订单相关
router.register(r'orders', OrderViewset, basename='orders')

# 轮播图url
router.register(r'banners', BannerViewset, basename='banners')

# 首页商品系列数据
router.register(r'indexgoods', IndexCategoryViewset, basename='indexgoods')

urlpatterns = [
    # drf自带的token认证模式
    re_path(r'^api-token-auth/', views.obtain_auth_token),
    # jwt的认证接口
    re_path(r'^login/$', obtain_jwt_token),
    re_path(r'^xadmin/', xadmin.site.urls),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'', include(router.urls)),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    re_path(r'docs/', include_docs_urls(title='vue项目')),
    re_path(r'^alipay/return/', AlipayView.as_view(), name='alipay'),

    re_path(r'^index/', TemplateView.as_view(template_name='index.html'), name='index'),

    # 第三方登录
    re_path('', include('social_django.urls', namespace='social'))

]
