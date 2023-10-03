from django import forms

class ApprovalForm(forms.Form):
    firstname = forms.CharField(max_length=15)
    lastname = forms.CharField(max_length=15)
    Dependants = forms.IntegerField()
    ApplicantIncome = forms.IntegerField()
    CoapplicantIncome = forms.IntegerField()
    LoanAmount = forms.IntegerField()
    Loan_Amount_Term = forms.IntegerField()
    Credit_History = forms.IntegerField()
    Gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
    Married = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    Education = forms.ChoiceField(choices=[('Graduated', 'Graduated'), ('Not_Graduated', 'Not_Graduated')])
    Self_Employed = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    Property_Area = forms.ChoiceField(choices=[('Rural', 'Rural'), ('Semiurban', 'Semiurban'), ('Urban', 'Urban')])