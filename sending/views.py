from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import Tag, CodeMobile, Client, Mailing, Message
from .serializer import TagSerializer, CodeMobileSerializer, ClientSerializer, MailingSerializer, MessageSerializer


class TagViews(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class SingleTagView(RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class CodeMobileViews(ListCreateAPIView):
    queryset = CodeMobile.objects.all()
    serializer_class = CodeMobileSerializer


class SingleCodeMobileView(RetrieveUpdateDestroyAPIView):
    serializer_class = CodeMobileSerializer
    queryset = CodeMobile.objects.all()


class ClientViews(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class SingleClientView(RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class MailingViews(ListCreateAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class SingleMailingViews(RetrieveUpdateDestroyAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer



class MessageViews(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MailingViews(ListCreateAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class SingleMailingViews(RetrieveUpdateDestroyAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

