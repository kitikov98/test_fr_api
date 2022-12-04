from rest_framework import serializers
from django.core.validators import MinValueValidator, MaxValueValidator


from .models import Tag, CodeMobile, Client, Mailing, Message

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['tag_id', 'tag']


class CodeMobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeMobile
        fields = ['codemobile_id', 'code_mobile']

class ClientSerializer(serializers.ModelSerializer):
    full_phone = serializers.ReadOnlyField(source="get_phone")

    class Meta:
        model = Client
        fields = ['client_id', 'tag', 'phone', 'code_mobile', 'time_zone', 'full_phone']

class MailingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mailing
        fields = ['mailing_id', 'date_start', 'date_end', 'text_message', 'tag_mailing', 'code_mailing']

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['message_id', 'date_send', 'status', 'mailing_id', 'client_id']
