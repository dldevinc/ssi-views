# ssi-views
A simple Django application to process SSI includes

[![PyPI](https://img.shields.io/pypi/v/ssi-views.svg)](https://pypi.org/project/ssi-views/)
[![Build Status](https://travis-ci.org/dldevinc/ssi-views.svg?branch=master)](https://travis-ci.org/dldevinc/ssi-views)

## Compatibility
* `django` >= 1.11
* `python` >= 3.5

## Features
* Supported Function-Based and Class-Based Views
* One URL pattern ~~to rule them all~~ for all SSI views
* Jinja2 support

## Installation
Install the package via Pip:

```
pip install ssi-views
```

Add it to your `INSTALLED_APPS` list:

```python
INSTALLED_APPS = (
    ...
    'ssi_views',
)
```

Add `ssi_views.urls` to your URLconf:

```python
urlpatterns = patterns('',
    ...

    # Django >= 2.0
    path('ssi/', include('ssi_views.urls')),

    # Django < 2.0
    url(r'^ssi/', include('ssi_views.urls', namespace='ssi_views')),
)
```

## Usage
#### @ssi_view
Use this decorator to register your views (Function-Based or Class-Based).
```python
from ssi_views.decorators import ssi_view

@ssi_view('myapp.form')
def form_view(request):
    ...

@ssi_view('myapp.form_cbv')
class SSIFormView(FormView):
    ...
```
**NOTE**: Each view must have a **unique** name.

You can combine `ssi_view` with other decorators.
```python
@csrf_exempt
@require_POST
@ssi_view('myapp.contact_form')
def csrf_exempt_view(request):
    # ...
```

#### {% ssi_url %}
```djangotemplate
{% load ssi_views %}

<!--# include virtual="{% ssi_url 'myapp.form' %}" -->
```

#### {% ssi_include %}
Template tag to render SSI `include` directive.
```djangotemplate
{% load ssi_views %}

{% ssi_include "myapp.form" %}
```

Output:
```html
<!--# include virtual="/ssi/myapp.form/" -->
```

#### Multiple names for the same view
```python
from ssi_views.decorators import ssi_view

@ssi_view(['myapp.form', 'myapp.fallback'])
def example_view(request):
    ...
```

## Jinja2 support
Enable Jinja2 extension
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'OPTIONS': {
            'extensions': [
                ...
                'ssi_views.templatetags.ssi_views.SSIIncludeExtension',
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

## Development and Testing
After cloning the Git repository, you should install this
in a virtualenv and set up for development:
```shell script
virtualenv .venv
source .venv/bin/activate
pip install -r ./requirements.txt
pre-commit install
```
