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


@register.inclusion_tag('tmp3.html')
def show_results(poll):
    choices = poll
    return {'choices1': choices}


@register.inclusion_tag(filename='tmp3.html', takes_context=True)  # takes_context=True来直接使用context里的变量
def do_results(context):
    print(type(context))
    # choices = context['poll3']
    choices = 10000000

    return {'choices': choices}


@register.tag(name="format_time")
def do_format_time(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, date_to_be_formatted, format_string = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires exactly two arguments" % token.contents.split()[0]
        )
    if not (format_string[0] == format_string[-1] and format_string[0] in ('"', "'")):
        raise template.TemplateSyntaxError(
            "%r tag's argument should be in quotes" % tag_name
        )
    return FormatTimeNode(date_to_be_formatted, format_string[1:-1])


class FormatTimeNode(template.Node):
    def __init__(self, date_to_be_formatted, format_string):
        self.date_to_be_formatted = template.Variable(date_to_be_formatted)
        self.format_string = format_string

    def render(self, context):
        try:
            actual_date = self.date_to_be_formatted.resolve(context)
            return actual_date.strftime(self.format_string)
        except template.VariableDoesNotExist:
            return ''
# https://blog.csdn.net/weixin_42134789/article/details/82772027