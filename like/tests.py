"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from utils.utils_func import add_app_testcase

modules = add_app_testcase(__name__.split('.')[0])
globals().update(modules)