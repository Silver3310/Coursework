import graphene
from graphene_django import DjangoObjectType

from polls.models import Question, Choice


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question


'''
# in the case we want to create our own types
class QuestionType(graphene.ObjectType):
    question_text = graphene.string()
    pub_date = graphene.types.datetime.DateTime()
'''


class ChoiceType(DjangoObjectType):
    class Meta:
        model = Choice


class CustomType(graphene.ObjectType):
    message = graphene.String()
    question_str = graphene.String()
    question = graphene.Field(QuestionType)

    def resolve_question_str(self, info):
        return self.question.__str__()
