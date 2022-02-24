from django.views.generic import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = "pages/home.html"

class About(TemplateView):
    template_name = "pages/about.html"
