"""
@author: shoo Wang
@contact: wangsuoo@foxmail.com
@file: urls.py
@time: 2020/6/6 0006
"""
from django.urls import path

from article import views

urlpatterns = [
    path('article/', views.index),
    path('details/<int:article_id>', views.get_detail_page)
]
