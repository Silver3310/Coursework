from django.views import generic
from django.views.generic.base import TemplateResponseMixin

from .models import Question
from .models import Choice
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


class ResultView(TemplateResponseMixin, generic.View):
    """
    TemplateResponseMixin provides render_to_response and template_name
    """
    template_name = 'polls/results.html'

    @staticmethod
    def get_queryset(question_id):
        return Question.objects.get(pk=question_id)

    def get(self, request, pk):
        queryset = self.get_queryset(pk)
        context = {'question': queryset}
        return self.render_to_response(context)
