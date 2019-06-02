from django.conf.urls.defaults import *
import views
from django.urls import path


urlpatterns = [
    path('', 'subscription.views.subscription_list', {}, 'subscription_list'),
    path('done/', 'django.views.generic.simple.direct_to_template',
            dict(template='subscription/subscription_done.html'), 'subscription_done'),
    path('change-done/', 'django.views.generic.simple.direct_to_template',
            dict(template='subscription/subscription_change_done.html',
            extra_context=dict(cancel_url=views.cancel_url)), 'subscription_change_done'),
    path('cancel/', 'django.views.generic.simple.direct_to_template',
            dict(template='subscription/subscription_cancel.html'), 'subscription_cancel'),
]

