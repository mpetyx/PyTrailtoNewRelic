PyTrailtoNewRelic
=================

A python hack for PaperTrail service to connect the logs in your New Relic system


Following some really nice documentation here, http://help.papertrailapp.com/kb/integrations/new-relic
I was able to create this simple hack for the newrelic python library (https://newrelic.com/docs/python/new-relic-for-python)

What it actually does, you can either apply to any function/view you want, (or if you are using django or flask just to the main application etc to the wsgi) 
and connect the logs it stores in the papertrail at the admin panel of new relic.
So, together with your performance you can have the exact log that trigger the original request.


For any more questions, please let an issue for me!!
