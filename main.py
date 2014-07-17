import os, sys, logging
os.environ["DJANGO_SETTINGS_MODULE"] = "potatoblogging.settings"
sys.path.append("/home/edson/Projetos/projetoPotatoBlog")

from google.appengine.ext.webapp import util
from django.conf import settings
settings._target = None

import django.core.handlers.wsgi
import django.core.signals
import django.db
import django.dispatch.dispatcher

def log_exception(*args, **kwds):
	logging.exception('Exception in request:')

django.dispatch.Signal.connect(
   django.core.signals.got_request_exception, log_exception)

django.dispatch.Signal.disconnect(
    django.core.signals.got_request_exception,
    django.db._rollback_on_exception)

def main():
	application = django.core.handlers.wsgi.WSGIHandler()
	util.run_wsgi_app(application)

if __name__ == "__main__":
	main()
