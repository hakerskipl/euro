#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import F, Count, Q
from django.http import HttpResponse, Http404
from django.core import serializers
from django.contrib.auth.forms import PasswordChangeForm
from web.models import *
from web.forms import *

# Create your views here.
def home(request):
	return HttpResponse('hi!')