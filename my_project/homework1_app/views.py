from django.shortcuts import render
from django.http import HttpResponse


def view_homepage(request):
    info = """<h1>Homepage of my first Django app</h1>
    <h2>Some important information</h2>
    <h2>Some not so important information</h2>
    <h3>Basement</h3>
    """
    return HttpResponse(info)


def get_about(request):
    info = """<h1>This is the ABOUT page</h1>
    <h2>And some more information</h2>
    <h3>Will anyone ever read this?!<h3>
    <p3>I'm Slim Shady, yes, i'm the real Shady!\n
    All you other Slim Shadys are just imitating!</p3>
    """
    return HttpResponse(info)
