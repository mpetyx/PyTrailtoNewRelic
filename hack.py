__author__ = 'mpetyx'

from newrelic import agent
import time
import socket

def add_papertrail_new_relic_custom_parameter():

    current_time = str(time.time())
    hostname = socket.gethostname()
    log_url = "https://papertrailapp.com/systems/%s/events?time=%s"%(hostname,current_time)
    agent.add_custom_parameter("log_url" , log_url)

    return True


# print(add_papertrail_new_relic_custom_parameter())

# The method calls add_custom_parameters, which is part of New Relic's Ruby Agent. The method returns true because it is meant to be called as a controller callback.
#
# Second, ensure that the new method is called during each request (or those which you would like to be linked). Add a before_filter to the top of the ApplicationController class definition, like this:
#
# def before_filter :add_papertrail_new_relic_custom_parameter
# end
# Deploy this code change a