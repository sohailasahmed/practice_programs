from django import forms

class calform(forms.Form):
    num1=forms.CharField(label="Value 1",widget=forms.NumberInput({'class':'form-control'}))
    opr=forms.ChoiceField(label="Operator",
                        choices=[
                            ('add','+'),
                            ('sub','-'),
                            ('mul','*'),
                            ('div','/'),
                            ('mod','%'),
                            ('pow','**'),
                        ],
                        widget=forms.Select)
    num2=forms.CharField(label="Value 2",widget=forms.NumberInput({'class':'form-control'}))
    submit=forms.CharField(label="",widget=forms.widgets.Input(attrs={'type':'submit','value':'Submit'}))