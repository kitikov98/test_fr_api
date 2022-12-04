from django.db import models
import uuid
import pytz
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Tag(models.Model):
    tag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag = models.TextField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.tag}'

class CodeMobile(models.Model):
    codemobile_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code_mobile = models.IntegerField(
        unique=True,
        default=1,
        validators=[
            MaxValueValidator(999),
            MinValueValidator(1)
        ]
     )

    def __str__(self):
        return f'{self.code_mobile}'


class Client(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    client_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.DecimalField(max_digits=7, decimal_places=0)
    tag = models.ForeignKey(Tag, to_field='tag', related_name='client_tag', on_delete=models.CASCADE)
    code_mobile = models.ForeignKey(CodeMobile, to_field='code_mobile', related_name='client_code_mobile',  on_delete=models.CASCADE)
    time_zone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
    full_phone = models.CharField(max_length=255)

    @property
    def get_phone(self):
        self.full_phone = '7'+str(self.code_mobile)+str(self.phone)
        return self.full_phone

    def __str__(self):
        return f'{self.client_id}'

class Mailing(models.Model):
    mailing_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_start = models.DateTimeField(default=datetime.now())
    date_end = models.DateTimeField(default=datetime.now())
    text_message = models.TextField(max_length=1000)
    tag_mailing = models.ForeignKey(Tag, to_field='tag', related_name='tag_mailing', on_delete=models.CASCADE)
    code_mailing = models.ForeignKey(CodeMobile, to_field='code_mobile', related_name='code_mailing',  on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.mailing_id}'

class Message(models.Model):
    message_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    date_send = models.DateTimeField(default=datetime.now())
    status = models.BooleanField(default=None)
    mailing_id = models.ForeignKey(Mailing, related_name='mailing', on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, related_name='client', on_delete=models.CASCADE)



# Create your models here.
