from django.shortcuts import render, render_to_response

# Create your views here.
from django.template.context import RequestContext
from project.settings import get_env_variable


def common(req):

    return render_to_response('homepage/index.html', {
        "CDOWM_API_ENDPOINT": get_env_variable("CDOWM_API_ENDPOINT"),
    }, RequestContext(req))

