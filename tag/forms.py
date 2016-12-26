# -*- coding: utf-8 -*-


from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)


class TagForm(forms.Form):
    def clean(self):
        print (self.request())
