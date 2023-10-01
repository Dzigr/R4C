from django import forms


class OrderForm(forms.Form):
    robot_serial = forms.CharField(max_length=5, required=True)
    email = forms.EmailField(max_length=255, required=True)
