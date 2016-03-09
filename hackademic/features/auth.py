from lettuce import *
from lxml.html import fromstring, submit_form
from django.test.client import Client
from nose.tools import assert_equals
from lettuce.django import django_url
from bs4 import BeautifulSoup

@before.all
def set_browser():
	world.browser = Client()

@step(r'I access the url "(.*)"')
def access_url(step, url):
	response = world.browser.get(url)
	world.dom = fromstring(response.content)

@step(r'I see the text "(.*)"')
def see_text(step, text):
	got = world.dom.get_element_by_id('heading').text_content()
	assert text == got

@step(r'I don\'t see the text "(.*)"')
def see_text(step, text):
	got = world.dom.get_element_by_id('heading').text_content()
	assert text != got

@step(r'I fill username "(.*)"')
def fill_username(step, user):
	world.dom.forms[0].inputs['username'].value = user

@step(r'I fill pwd "(.*)"')
def fill_username(step, pwd):
	world.dom.forms[0].inputs['password'].value = pwd

@step(r'I fill email "(.*)"')
def fill_username(step, email):
	world.dom.forms[0].inputs['email'].value = email

@step(r'I fill type "(.*)"')
def fill_username(step, type_):
	world.dom.forms[0].inputs['type'].value = type_

@step(r'I press "Submit"')
def submit(step):
	world.dom.forms[0].action = 'http://localhost:8000/register/'
	world.dom = fromstring(submit_form(world.dom.forms[0]).read())
	print world.dom

@step(r'I press "Login"')
def submit(step):
	world.dom.forms[0].action = 'http://localhost:8000/login/'
	world.dom = fromstring(submit_form(world.dom.forms[0]).read())
	print world.dom