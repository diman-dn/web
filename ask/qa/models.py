from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.http import HttpResponse
def test(request, *args, **kwargs):
	return HttpResponse('OK')
