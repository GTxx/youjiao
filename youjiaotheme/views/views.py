# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator
from mezzanine.blog.models import *
from mezzanine.pages.models import *


# Create your views here.

def activities(request, sub_node, page_no):
    template_name = 'activities/index.html'

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

        blogs_with_page = Paginator(blogs_with_category, 10)
        count = blogs_with_page.count
        num_pages = blogs_with_page.num_pages

        if int(page_no) > num_pages:
            raise Http404('404 not found')

        blogs = blogs_with_page.page(page_no).object_list

        obj = {'blogs': blogs, 'count': count, 'num_page': num_pages, 'page': page_no}

        return render(request, template_name, obj)

    except:
        raise Http404('404 not found')


def blog_detail(request, blog_id):
    template_name = 'activities/blog.html'

    try:
        blog = BlogPost.objects.filter(id=blog_id).filter(status=2)[0]
        return render(request, template_name, {'blog': blog})

    except:
        raise Http404('404 not found')


def products(request, sub_node):
    template_name = 'products/index.html'

    page_map = {
        'textbook': '幼教教材',
        'readbook': '幼教读物',
        'toy': '幼教玩具',
        'equipment': '教学设备展示',
        'other': '其他婴幼儿产品'
    }

    try:
        current_page = page_map[sub_node]
        page_obj = RichTextPage.objects.filter(title=current_page).filter(status=2)[0]
        return render(request, template_name, {'page_content': page_obj.content})

    except:
        raise Http404('404 not found')


def text_book_detail(request):
    template_name = 'products/textbook_detail.html'

    return render(request, template_name)
