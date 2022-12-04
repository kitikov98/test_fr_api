from django.urls import path, include
from .views import TagViews, SingleTagView,  CodeMobileViews, SingleCodeMobileView, ClientViews, SingleClientView, MailingViews, SingleMailingViews, MessageViews


urlpatterns = [
    path('tag/', TagViews.as_view()),
    path('tag/<uuid:pk>', SingleTagView.as_view()),
    path('code_mobile/', CodeMobileViews.as_view()),
    path('code_mobile/<uuid:pk>', SingleCodeMobileView.as_view()),
    path('client/', ClientViews.as_view()),
    path('client/<uuid:pk>', SingleClientView.as_view()),
    path('mailing/', MailingViews.as_view()),
    path('mailing/<uuid:pk>', SingleMailingViews.as_view()),
    path('message/', MessageViews.as_view())
]