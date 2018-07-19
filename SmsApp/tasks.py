from __future__ import absolute_import
from celery import shared_task
from MailApp.models import *
from django.forms.models import model_to_dict

@shared_task(name='tasks.send_sms')
class send_sms:

	def __init__(self,notif_id):
		self.notif_id   = notif_id
		self.send()

	def send(self):
		print "Sending sms to user"
		obj = NotificationRetry.objects.get(id=self.notif_id)




