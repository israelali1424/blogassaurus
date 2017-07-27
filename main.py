#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import jinja2
import os
import webapp2
import logging
from google.appengine.api import users



jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

def makeHeader():
    user = users.get_current_user()
    if user:
        nickname = user.nickname()
        logout_url = users.create_logout_url('/')
        greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
            nickname, logout_url)

    else:
        login_url = users.create_login_url('/')
        greeting = '<a href="{}">Sign in</a>'.format(login_url)

    return greeting

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = makeHeader()
        template_vars = {'greeting': header}

        template = jinja_environment.get_template('templates/Israel.html')
        self.response.write(template.render(template_vars))

class IsraelInfo(webapp2.RequestHandler):
    def get(self):
        header = makeHeader()
        template_vars = {'greeting': header}
        template = jinja_environment.get_template('templates/Bio.html')
        self.response.write(template.render(template_vars))

class ContactIsrael(webapp2.RequestHandler):
    def get(self):
        header = makeHeader()
        template_vars = {'greeting': header}
        template = jinja_environment.get_template('templates/Contact.html')
        self.response.write(template.render(template_vars))


class IsraelBlog(webapp2.RequestHandler):
    def get(self):
        header = makeHeader()
        template_vars = {'greeting': header}
        template = jinja_environment.get_template('templates/Blog.html')
        self.response.write(template.render(template_vars))

class Hello(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/hello.html')
        self.response.write(template.render())


class SurveyHandler(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('survey/Survey_input.html')
        self.response.write(template.render())

    def post(self):
        template = jinja_environment.get_template('survey/Survey_output.html')
        survey_dict = {
          'name_answer': self.request.get('name'),
          'age_answer': self.request.get('age'),
          'location_answer': self.request.get('location'),
          'school_answer': self.request.get('school_answer'),
          'fun_fact_answer': self.request.get('fun_fact_answer')}
        self.response.write(template.render(survey_dict))

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                nickname, logout_url)
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)

        self.response.write(
            '<html><body>{}</body></html>'.format(greeting))


class AdminPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            if users.is_current_user_admin():
                self.response.write('You are an administrator.')
            else:
                self.response.write('You are not an administrator.')
        else:
            self.response.write('You are not logged in.')



app = webapp2.WSGIApplication([
    ('/', MainHandler), #HomePage
    ('/Bio.html',IsraelInfo),
    ('/Israel.html',MainHandler),
    ('/Contact.html',ContactIsrael),
    ('/Blog.html',IsraelBlog),
    ('/hello.html',Hello),
    ('/Survey_input.html',SurveyHandler),
    ('/',MainPage),
    ('/Adim',AdminPage)

], debug=True)
