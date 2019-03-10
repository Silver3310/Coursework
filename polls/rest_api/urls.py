from rest_framework import routers

from polls.rest_api import views


router = routers.DefaultRouter()
router.register(
    r'question',
    views.QuestionViewSet
)
router.register(
    r'custom_question',
    views.CustomQuestionView,
    base_name='poll'
)
router.register(
    r'choice',
    views.ChoiceViewSet
)
