# imports

from typing import Dict, Any

from django.shortcuts import render
from django.http import HttpRequest


def sign_in_with_oauth(request: HttpRequest):
    """
    View to display template where users can proceed with their authentication using oAuth.
    """

    context: Dict[str, Any] = {

    }  # view context data

    return render(request, "myapp/index.html", context)
