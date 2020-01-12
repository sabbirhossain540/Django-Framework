from django import forms
from django.core import validators

#Customized Validation for Input Box
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Need To Start With Z")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    varifyEmail = forms.EmailField(label='Enter Your Email Again:')
    text = forms.CharField(widget=forms.Textarea)

    #Hidden Input Validation
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    #Email Match Validation
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['varifyEmail']

        if email != vemail:
            raise forms.ValidationError("Make Sure Email Match!")


    #Customized Validator
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("Gotcha Bot!")
    #
    #     return botcatcher
