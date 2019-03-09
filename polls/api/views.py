from rest_framework import viewsets
from rest_framework.response import Response

from polls.models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('-pub_date')
    serializer_class = QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class CustomQuestionView(viewsets.ViewSet):
    def list(self, request, format=None):
        """
        request: DRF request
        format: JSON or XML, None is a browsable API
        """
        questions = [
            question.question_text for question in Question.objects.all()
        ]
        return Response(questions)
