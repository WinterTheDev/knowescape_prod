from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="home"),
    path('start-up', views.start_up, name="start-up"),
    path('contact', views.contact, name="contact"),
    path('signup/learner', views.learner_signup, name="learner-signup"),
    path('signup/company', views.company_signup, name="company-signup"),
    path('enterprise-supplier-dev', views.es_dev, name="es-dev"),
    path('skills-dev', views.skills_dev, name="skills-dev"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)