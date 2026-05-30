from django import forms

class calform(forms.Form):
    Name=forms.CharField(label="Subject",widget=forms.TextInput({'class':'form-control'}))
    Description=forms.CharField(label="Message",widget=forms.Textarea({'class':'form-control'}))