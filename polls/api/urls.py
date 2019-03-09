from rest_framework import routers

from polls.api import views


router = routers.DefaultRouter()
router.register(r'question', views.QuestionViewSet)
router.register(r'choice', views.ChoiceViewSet)
