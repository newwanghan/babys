import logging

from django.shortcuts import render
from django.views.generic import TemplateView

from commodity.models import *


def indexView(request):
    title = '首页'
    classContent = ''
    commodityInfos = CommodityInfos.objects.order_by('-sold').all()[:8]
    types = Types.objects.all()

    # 宝宝服饰
    cl = [x.seconds for x in types if x.firsts == '儿童服饰']
    clothes = CommodityInfos.objects.filter(types__in=cl).order_by('-sold')[:5]

    # 奶粉辅食
    fl = [x.seconds for x in types if x.firsts == '奶粉辅食']
    food = CommodityInfos.objects.filter(types__in=fl).order_by('-sold')[:5]

    # 宝宝用品
    gl = [x.seconds for x in types if x.firsts == '儿童用品']
    goods = CommodityInfos.objects.filter(types__in=gl).order_by('-sold')[:5]
    return render(request, 'index.html', locals())


class indexClassView(TemplateView):
    template_name = 'index.html'
    template_engine = None
    content_type = None
    extra_context = {'title': '首页', 'classContent': ''}

    # 重新定义模板上下文的获取方式
    def get_context_data(self, **kwargs):
        uqalogger = logging.getLogger('get_context_data')
        context = super().get_context_data(**kwargs)
        context['commodityInfos'] = CommodityInfos.objects.order_by('-sold').all()[:8]
        types = Types.objects.all()
        # uqalogger.info(context)
        # uqalogger.info(types)
        
        # 宝宝服饰
        cl = [x.seconds for x in types if x.firsts == '儿童服饰']
        context['clothes'] = CommodityInfos.objects.filter(types__in=cl).order_by('-sold')[:5]
        # 奶粉辅食
        fl = [x.seconds for x in types if x.firsts == '奶粉辅食']
        context['food'] = CommodityInfos.objects.filter(types__in=fl).order_by('-sold')[:5]
        # 宝宝用品
        gl = [x.seconds for x in types if x.firsts == '儿童用品']
        context['goods'] = CommodityInfos.objects.filter(types__in=gl).order_by('-sold')[:5]
        # uqalogger.info(context)
        return context

    # 定义HTTP的GET请求处理方法
    # 参数request代表HTTP请求信息
    # 若路由设有路由变量，则可从参数kwargs里获取
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    # 定义HTTP的POST请求处理方法
    # 参数request代表HTTP请求信息
    # 若路由设有路由变量，则可从参数kwargs里获取
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


def bad_request(request, exception):
    """ 400 error handler. """
    return render(request, '404.html', status=400)


def permission_denied(request, exception):
    """ Permission denied (403) handler. """
    return render(request, '404.html', status=403)


def page_not_found(request, exception):
    return render(request, '404.html', status=404)


def server_error(request):
    """ 500 error handler. """
    return render(request, '404.html', status=500)
