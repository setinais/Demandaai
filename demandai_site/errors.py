from django.shortcuts import render_to_response

def handler404(request, template_name="site/error.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response


def handler500(request, template_name="site/error.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response

