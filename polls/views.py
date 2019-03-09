from django.views import generic

from .models import Question
from .mixins import RequireLoginMixin


class IndexView(RequireLoginMixin, generic.ListView):
    """
    Whenever this view launches, RequireLoginMixin will now be checked for methods
    """
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """
    Automatically checks if a question doesn't exist, it includes the 404 error
    """
    model = Question
    template_name = 'polls/detail.html'


class DeleteView(generic.DeleteView):
    model = Question
    success_url = '/polls/'
