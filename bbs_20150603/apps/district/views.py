from django.views import generic
from apps.district.models import District
from apps.forum.models import Forum
from apps.account.models import User
from apps.article.models import Article



class DistrictListView(generic.TemplateView):
    template_name = "district/district_list.html"

    def get_context_data(self, **kwargs):
        context = super(DistrictListView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        context['users'] = User.objects.all()
        context['districts'] = District.objects.all()
        context['forums'] = Forum.objects.all()


        return context





