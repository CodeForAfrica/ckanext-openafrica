from flask import Blueprint
from ckan.plugins.toolkit import render

openafrica = Blueprint('openafrica', __name__)

def toc():
    return render('home/about/toc.html')

def accessibility():
    return render('home/about/accessibility.html')

def coc():
    return render('home/about/coc.html')

def moderation():
    return render('home/about/moderation.html')

def faq():
    return render('home/about/faq.html')

def privacy():
    return render('home/about/privacy.html')

def contact():
    return render('home/about/contact.html')

def atlas():
    return render('atlas.html')

rules = [
    ("/about/terms-and-conditions", "toc", toc),
    ("/about/accessibility", "accessibility", accessibility),
    ("/about/code-of-conduct", "coc", coc),
    ("/about/moderation-policy", "moderation", moderation),
    ("/about/faq", "faq", faq),
    ("/about/privacy", "privacy", privacy),
    ("/about/contact", "contact", contact)
]

for rule in rules:
    openafrica.add_url_rule(*rule)

