from django import template
from commodity.models import *

register = template.Library()


class ReversalNode(template.Node):
    def __init__(self, value):
        self.value = str(value)

    def render(self, context):
        return self.value[::-1]



@register.tag(name='reversal')
def do_reversal(parse, token):
    try:
        tag_name, value = token.split_contents()
    except:
        raise template.TemplateSyntaxError('syntax')
    return ReversalNode(value)



# use simple tag to show string 一个返回string
@register.simple_tag
def total_articles():
    return CommodityInfos.objects.filter(sezes__contains='色').count()

# use simple tag to set context variable 一个给模板context传递变量
@register.simple_tag
def get_first_article():
    return CommodityInfos.objects.filter(sezes__contains='色').order_by('-price')[0]


# show rendered template 一个显示渲染过的模板
@register.inclusion_tag(filename='tmp2.html')
def show_latest_articles(count=5):
    latest_articles = CommodityInfos.objects.filter(sezes__contains='色').order_by('-price')[:count]
    return {'latest_articles': latest_articles}
