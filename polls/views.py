from django.views import generic
from django.views.generic.base import TemplateResponseMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse

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


class VoteView(generic.View):
    """
    A view to vote for a particular choice in a question
    """

    @staticmethod
    def get_queryset(choice_id):
        return Choice.objects.get(pk=choice_id)

    def post(self, request, pk):
        question_id = pk
        choice_id = request.POST.get(
            'choice',
            None
        )
        try:
            queryset = self.get_queryset(choice_id)
        except (KeyError, Choice.DoesNotExist):
            return redirect(reverse('detail', kwargs={'pk': question_id}))
        else:
            queryset.votes += 1
            queryset.save()
            return redirect(reverse('vote_result', kwargs={'pk': question_id}))


class SwitchboardView(generic.View):
    """
    Combines two views, ResultView for GET requests, VoteView for POST requests
    """

    @staticmethod
    def get(request, pk):
        view = ResultView.as_view()
        return view(request, pk)

    @staticmethod
    def post(request, pk):
        view = VoteView.as_view()
        return view(request, pk)
