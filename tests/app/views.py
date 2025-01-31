from django.http import HttpResponse
from django.views.decorators.cache import cache_control, never_cache
from django.views.decorators.http import require_GET
from django.views.generic import TemplateView, View

from ssi_views.decorators import ssi_view


class IndexView(TemplateView):
    template_name = "app/index.html"


@ssi_view("tests.simple")
def simple_view(request):
    return HttpResponse(b"I hear the drums echoing tonight")


@ssi_view("tests.simple")
def simple_override_view(request):
    return HttpResponse(b"But she hears only whispers of some quiet conversation")


@require_GET
@ssi_view("tests.method-get")
def get_view(request):
    return HttpResponse(b"She's coming in twelve-thirty flight")


@ssi_view("tests.cached")
@cache_control(max_age=0, s_maxage=30, must_revalidate=True)
def cached_view(request):
    return HttpResponse(
        b"Her moonlit wings reflect the stars that guide me towards salvation"
    )


@never_cache
@ssi_view("tests.never_cached")
def decorated_view(request):
    return HttpResponse(b"I stopped an old man along the way")


@ssi_view(["tests.first", "tests.second", "tests.third"])
def multinamed_view(request):
    return HttpResponse(b"Hoping to find some old forgotten words or ancient melodies")


@ssi_view(["tests.foo", "tests.bar", "tests.baz"])
def another_multinamed_view(request):
    return HttpResponse(
        b"He turned to me as if to say: Hurry boy, it's waiting there for you"
    )


@ssi_view("tests.simple_cbv")
class SimpleView(View):
    def get(self, request):
        return HttpResponse(b"There's nothing that a hundred men or more could ever do")
