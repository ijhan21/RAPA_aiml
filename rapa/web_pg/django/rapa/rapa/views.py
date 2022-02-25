from django.views.generic.base import TemplateView

#--- TemplateView
class HomeView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_list'] = ['polls', 'gogo', 'new']
        return context