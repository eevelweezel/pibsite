from django.conf import settings
from django.template.response import TemplateResponse


def home(request):
    context = {'WEBSSH': settings.WEBSSH_URL}
    headers = {'Content-Security-Policy': f"base-uri 127.0.0.1"}
    return TemplateResponse(
               request,
               'base.html',
               context=context,
               headers=headers
    )

