from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(('index.urls', 'index'), namespace='index')),
    path('commodity/', include(('commodity.urls', 'commodity'), namespace='commodity')),
    path('shopper/', include(('shopper.urls', 'shopper'), namespace='shopper')),
    path('test01/', include(('test01.urls', 'test01'), namespace='test01')),

    # 定义媒体资源的路由信息
    re_path(r"media/(?P<path>.*)", serve, {"document_root": settings.MEDIA_ROOT}, name='media'),
    # 定义静态资源的路由信息
    re_path('static/(?P<path>.*)', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
]

handler400 = "index.views.page_not_found"
handler403 = "index.views.page_not_found"
handler404 = "index.views.page_not_found"
handler500 = "index.views.server_error"
