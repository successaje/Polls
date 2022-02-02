from django.urls import path
from .views import polls_list, polls_detail

from .apiviews import PollList, PollDetail, ChoiceList, CreateVote

#There are 3 API endproints

urlpatterns = [
    path('polls/', PollList.as_view(), name='polls_list'),
    path('polls/<int:pk>/', PollDetail.as_view(), name='polls_detail'),
    path("choices/", ChoiceList.as_view(), name="choice_list"),
    path("vote/", CreateVote.as_view(), name="create_vote"),
]