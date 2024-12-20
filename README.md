# ssi-views

A simple Django application to process SSI includes.

[![PyPI](https://img.shields.io/pypi/v/ssi-views.svg)](https://pypi.org/project/ssi-views/)
[![Build Status](https://github.com/dldevinc/ssi-views/actions/workflows/tests.yml/badge.svg)](https://github.com/dldevinc/ssi-views)
[![Software license](https://img.shields.io/pypi/l/ssi-views.svg)](https://pypi.org/project/ssi-views/)

## Compatibility

-   `python` >= 3.9
-   `django` >= 3.2

## Features

-   Supported Function-Based and Class-Based Views
-   One URL pattern ~~to rule them all~~ for all SSI views
-   Jinja2 support

## Installation

Install the latest release with pip:

```shell
pip install ssi-views
```

Add `ssi_views` to your INSTALLED_APPS in django's `settings.py`:

```python
INSTALLED_APPS = [
    "ssi_views",
]
```

Add `ssi_views.urls` to your URLconf:

```python
from django.urls import include, path

urlpatterns = [
    path("ssi/", include("ssi_views.urls")),
]
```

## Usage

#### @ssi_view("name")

Use this decorator to register your views (Function-Based or Class-Based).

```python
from ssi_views.decorators import ssi_view

@ssi_view("myapp.form")
def form_view(request):
    ...

@ssi_view("myapp.form_cbv")
class SSIFormView(FormView):
    ...
```

**NOTE**: The specified name has to be unique.

You can combine `ssi_view` with other decorators:

```python
@csrf_exempt
@require_POST
@ssi_view("myapp.contact_form")
def csrf_exempt_view(request):
    # ...
```

#### {% ssi_include %}

Template tag to render `<!--# include virtual="..." -->` directive.

```djangotemplate
{% load ssi_views %}

{% ssi_include "myapp.form" %}
```

Output:

```html
<!--# include virtual="/ssi/myapp.form/" -->
```

#### {% ssi_url %}

This tag is used to add SSI URLs in the template files:

```djangotemplate
{% load ssi_views %}

<!--# include virtual="{% ssi_url 'myapp.form' %}" -->
```

#### Multiple names

You can have multiple names for the same view:

```python
from ssi_views.decorators import ssi_view

@ssi_view(["myapp.form", "myapp.fallback"])
def example_view(request):
    ...
```

## Jinja2 support

Enable Jinja2 extension

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.jinja2.Jinja2",
        "OPTIONS": {
            "extensions": [
                ...
                "ssi_views.templatetags.ssi_views.SSIIncludeExtension",
            ]
        }
    }
]
```

**NOTE**: If you are using [django-jinja](https://niwinz.github.io/django-jinja/latest/), you don't need to do this.

The usage is similar to Django, except that `ssi_url` is a global function:

```jinja2
<!--# include virtual="{{ ssi_url('myapp.form') }}" -->
```
