from flask import Blueprint, make_response
from ckan.plugins.toolkit import render

openafrica = Blueprint("openafrica", __name__)

def static_path(path):
    def render_path():
        return render(path)

    return render_path

def robots_txt():
    '''display robots.txt'''
    resp = make_response(render("robots.txt"))
    resp.headers["Content-Type"] = "text/plain; charset=utf-8"
    return resp

rules = [
    ("/about/terms-and-conditions", "toc", static_path("home/about/toc.html")),
    ("/about/accessibility", "accessibility", static_path("home/about/accessibility.html")),
    ("/about/code-of-conduct", "coc", static_path("home/about/coc.html")),
    ("/about/moderation-policy", "moderation", static_path("home/about/moderation.html")),
    ("/about/faq", "faq", static_path("home/about/faq.html")),
    ("/about/privacy", "privacy", static_path("home/about/privacy.html")),
    ("/about/contact-us", "contact", static_path("home/about/contact.html")),
    ("/robots.txt", "robots_txt", robots_txt())
]

for rule in rules:
    openafrica.add_url_rule(*rule)

