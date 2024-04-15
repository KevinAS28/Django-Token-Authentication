import json

from django.http import JsonResponse
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

from token_authentication.auth_core import token_auth

# Create your views here.
@token_auth(roles=['*'])
def helloworld(request:WSGIRequest):
    data = json.loads(request.body)
    if 'text' in data:
        if data['text'] == 'please':
            return {'text': 'Now you getting it'}
        else:
            return {'text': 'Your authentication is correct, but try put a magic word in your text field'}
    else:
        return {'text': 'Your authentication is correct, but there is no "text" field in your JSON request'}

@token_auth(roles=['user'], get_user=True)
def test(user: ta_models.UserAuthentication, request: WSGIRequest):
    return JsonResponse({'User': model_to_dict(user)})
