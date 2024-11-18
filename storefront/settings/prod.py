from storefront.settings.dev import SECRET_KEY
from .common import *
import os

SECRET_KEY=os.environ['SECRET_KEY']

DEBUG = False


ALLOWED_HOSTS=[]
