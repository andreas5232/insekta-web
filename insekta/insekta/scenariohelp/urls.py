from django.conf.urls import url

from insekta.scenariohelp import views


app_name = 'scenariohelp'
urlpatterns = [
    url(r'^$', views.list_questions, name='index'),
    url(r'^view/(\d+)$', views.view_question, name='view'),
    url(r'^my_questions$', views.my_questions, name='my_questions'),
    url(r'^scenario_questions/(.+)/(.+)$', views.scenario_questions, name='scenario_questions'),
    url(r'^new_question/(.+)/(.+)$', views.new_question, name='new_question'),
    url(r'^configure$', views.configure_help, name='configure_help'),
    url(r'^set_support_scenario/(.+)/(.+)$', views.set_support_scenario, name='set_support_scenario'),
]
