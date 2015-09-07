from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"

class IndexPage(generic.TemplateView):
    template_name = "index.html"

class Index2Page(generic.TemplateView):
    template_name = "index2.html"
