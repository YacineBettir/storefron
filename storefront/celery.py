from celery import Celery
import os

import celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE','storefront.settings.dev' )
celery= Celery()
celery.config_from_object('django.conf:settings',namespace='CELERY')
celery.autodiscover_tasks() 