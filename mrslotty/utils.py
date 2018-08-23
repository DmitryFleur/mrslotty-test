from .models import Urls
import requests


def get_url_status(url):
    if url.enabled is True:
        try:
            response = requests.get(url.url)
            return response.status_code
        except Exception:
            pass
    return None


def get_link(url):
    try:
        url = Urls.objects.get(url=url)
    except Urls.DoesNotExist:
        url = None
    return url
