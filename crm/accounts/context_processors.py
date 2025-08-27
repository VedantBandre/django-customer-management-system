from django.conf import settings

def site_brand(request):
    return {"SITE_NAME": getattr(settings, "SITE_NAME", "E-Corp CMS")}
