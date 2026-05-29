from django import forms

class calform(forms.Form):
    Name=forms.CharField(label="Laptop Name",widget=forms.TextInput({'class':'form-control'}))
    Description=forms.CharField(label="Description",widget=forms.Textarea({'class':'form-control'}))