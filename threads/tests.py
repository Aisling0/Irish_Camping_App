from django.test import TestCase
from home.views import get_index
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from .models import Subject


class HomePageTest(TestCase):
    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_index)

    def test_check_content_is_correct(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "index.html")
        home_page_template_output = render_to_response("../home/templates/../templates/index.html").content
        self.assertEqual(home_page.content, home_page_template_output)


class SubjectPageTest(TestCase):

    def test_check_content_is_correct(self):
        subject_page = self.client.get('/forum/')
        self.assertTemplateUsed(subject_page, "forum.html")
        subject_page_template_output = render_to_response("forum.html",
                                                          {'subjects':
                                                               Subject.objects.all()}).content
        self.assertEqual(subject_page.content, subject_page_template_output)