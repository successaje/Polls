from django.urls import path

from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, PollViewSet, UserCreate, LoginView
from .views import polls_list, polls_detail

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

schema_view = get_swagger_view(title='Polls API')

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

#There are 3 API endproints

#Also making it a nested structure

urlpatterns = [
    path('polls/', PollList.as_view(), name='polls_list'),
    path('polls/<int:pk>/', PollDetail.as_view(), name='polls_detail'),
    path("choices/", ChoiceList.as_view(), name="choice_list"),

    path("login/", LoginView.as_view(), name="login"),
    path("login/", views.obtain_auth_token, name="login"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("swagger-docs/", schema_view),
    path("docs/", include_docs_urls(title='Polls API')),

    #path("vote/", CreateVote.as_view(), name="create_vote"),
]

urlpatterns += router.urls
