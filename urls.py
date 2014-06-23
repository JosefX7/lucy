# -*- coding: utf-8 -*-
"""
Created on Sat Jun 21 12:30:59 2014

@author: Josef
"""

from django.conf.urls import patterns, include, url
from lucy import views
urlpatterns = patterns('',
        url(r'^$', views.index, name='index')

)