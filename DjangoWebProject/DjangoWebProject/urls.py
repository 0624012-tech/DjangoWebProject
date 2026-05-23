from django.urls import include, re_path
import HelloDjangoApp.views

urlpatterns = [
    re_path(r'^$', HelloDjangoApp.views.index, name='index'),
    re_path(r'^home$', HelloDjangoApp.views.index, name='home'),
    re_path(r'^about$', HelloDjangoApp.views.about, name='about'),
    re_path(r'^generate_outline$', HelloDjangoApp.views.generate_outline, name='generate_outline'),
    re_path(r'^assessments$', HelloDjangoApp.views.assessments, name='assessments'), 
]
