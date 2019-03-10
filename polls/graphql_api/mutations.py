from django.utils.timezone import now

import graphene

from polls.models import Question
from polls.graphql_api.types import QuestionType


class CreateQuestion(graphene.Mutation):

    class Arguments:
        question_text = graphene.String()

    ok = graphene.Boolean()
    question = graphene.Field(QuestionType)

    def mutate(self, info, question_text):
        """The method that must return a mutation"""
        question = Question(
            question_text=question_text,
            pub_date=now()
        )
        question.save()
        ok = True
        return CreateQuestion(
            question=question,
            ok=ok
        )


class MyMutations(graphene.ObjectType):
    # we wanna to tell Graphene
    # that whenever the create question function is used
    # we want to map it to this create question mutation
    create_question = CreateQuestion.Field()
