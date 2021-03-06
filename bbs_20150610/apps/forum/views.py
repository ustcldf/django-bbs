from django.http import HttpResponse
from django.views import generic
from apps.article.models import Article
from apps.forum.models import Forum
from apps.account.models import User





class HomeView(generic.ListView):
    model = Forum
    template_name = "forum/home.html"

    def get_context_data(self, **kwargs):
        # context = super(HomeView, self).get_context_data(**kwargs)
        # context.update(self.kwargs)
        #
        # context['count1'] = self.object_list.filter(forum=context['forum']).count()
        pass

def deleteForum(request):
    forum_id = request.POST.get('forum_id')
    forum = Forum.objects.get(id=forum_id)
    Article.objects.filter(forum=forum).delete()
    forum.delete()
    return HttpResponse('')



