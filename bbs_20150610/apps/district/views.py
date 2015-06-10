from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator
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



class CreateView(generic.TemplateView):
    template_name = "district/create.html"


    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['districts'] = District.objects.all()
        context['forums'] = Forum.objects.all()

        return context


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CreateView, self).dispatch(request, *args, **kwargs)

    def get_template_names(self):
        return "district/create_%s.html" % self.kwargs.get("tag")




class CreateDistrictView(generic.TemplateView):
    template_name = "district/createDistrict.html"

def createDistrict(request):
    pass


def deleteDistrict(request):
    district_id = request.POST.get('district_id')
    district = District.objects.get(id=district_id)
    forums = Forum.objects.filter(district=district)

    for forum in forums:
        Article.objects.filter(forum=forum).delete()
    forums.delete()
    district.delete()


    return HttpResponse('')

class SettingIcon(generic.TemplateView):
    template_name = "district/setting_icon.html"
