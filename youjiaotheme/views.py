# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import Http404
from mezzanine.blog.models import *
import math


# Create your views here.

def activities(request, sub_node, page_no):
    template_name = 'activities/index.html'

    page_size = 20
    start_page = (int(page_no) - 1) * page_size
    end_page = int(page_no) * page_size

    page_map = {
        'policy': '幼教政策',
        'news': '幼教新闻',
        'events': '幼教事件',
        'research': '理论研究',
        'activity': '实践活动'
    }

    try:
        category = page_map[sub_node]
        category_obj = BlogCategory.objects.filter(title=category)[0]
        # category_id = category_obj[0].id
        blogs_with_category = BlogPost.objects.filter(categories=category_obj).filter(status=2)
        count = blogs_with_category.count()
        blogs = blogs_with_category[start_page:end_page]

        page_all = math.ceil(count / float(page_size))

        obj = {'blogs': blogs, 'count': count, 'page_all': page_all, 'page': page_no}

        return render(request, template_name, obj)

    except:
        raise Http404("404 not found")


def blog_detail(request, blog_id):
    template_name = 'activities/blog.html'

    try:
        blog = BlogPost.objects.filter(id=blog_id)[0]

        return render(request, template_name, {'blog': blog})

    except:
        raise Http404("404 not found")
