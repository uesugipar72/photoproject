# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 08:00:41 2023

@author: user
"""

from django.forms import ModelForm
from .models import PhotoPost

class PhotoPostForm(ModelForm):
    
    class Meta:
        model = PhotoPost
        fields =['category','title','comment','image1','image2']
        