import graphene

from polls.models import Question
from polls.api.types import QuestionType
from polls.api.types import CustomType
from polls.api.mutations import MyMutations


class Query(graphene.ObjectType):
    # these attributes are how we name resolvers
    all_questions = graphene.List(QuestionType)
    # we expect a user to give us id (int)
    question = graphene.Field(
        QuestionType,
        id=graphene.Int()
    )
    custom_question = graphene.Field(
        CustomType,
        id=graphene.Int()
    )

    def resolve_all_questions(self, info):
        return Question.objects.all()

    def resolve_question(self, info, **kwargs):
        qid = kwargs.get('id')

        if qid is not None:
            return Question.objects.get(pk=qid)
        return None

    def resolve_custom_question(self, info, **kwargs):
        qid = kwargs.get('id')

        cq = CustomType()
        if qid is not None:
            question = Question.objects.get(pk=qid)
            # we don't define our question_str here
            # because it has its own built-in resolver
            # on the custom type
            cq.question = question
            cq.message = 'Query Succeeded!'
            return cq
        return None


schema = graphene.Schema(
    query=Query,
    mutation=MyMutations
)
