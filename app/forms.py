import os
from django import forms
from django.core.mail import send_mail
from app.models import Profile, Category, Item, Comment, Reply

class ContactForm(forms.Form):
    sender = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        sender = self.cleaned_data["sender"]
        message = self.cleaned_data["message"]
        subject = "Roblist Help"
        body = """
                Your assistance is required!
                From: {}
                Question: {}
               """.format(sender, message)
        recipient_list = [os.environ.get("EMAIL_HOST_USER")]
        send_mail(subject, body, sender, recipient_list)
