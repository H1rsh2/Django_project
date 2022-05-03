from django import forms
from .models import Stock
from .models import Provider
from .models import Food
from django.forms import ModelForm, TextInput, Textarea, MultipleChoiceField, CheckboxSelectMultiple, DateField, SelectDateWidget


class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = ["name_stock", "title", "stock", "stock_status", "dt"]
        widgets = {
            "name_stock": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            })},
        title = MultipleChoiceField(
            required=False,
            widget=CheckboxSelectMultiple (
                attrs={'class': 'form-control', 'placeholder': 'Выберите поставщика'}),
            choices=["title"],
            ),
        stock = MultipleChoiceField(
            required=False,
            widget=CheckboxSelectMultiple,
            choices=["stock"],
            ),
        stock_status = MultipleChoiceField(
            required=False,
            widget=CheckboxSelectMultiple,
            choices=["stock_status"],
            ),
        dt = DateField(
            widget=SelectDateWidget(
                empty_label=("Choose Year", "Choose Month", "Choose Day"),
            )
        ),


class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        fields = ["name", "type", "inn", "kpp", "mail", "phone", "address"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
        }
        type = MultipleChoiceField(
            required=False,
            widget=CheckboxSelectMultiple,
            choices=["type"],
        ),
        widgets = {
            "inn": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ИНН'
            }),
            "kpp": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ОГРН'
            }),
            "mail": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите почту'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите телефон'
            }),
            "address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес'
            }),
        }


class FoodForm(forms.Form):
    locations = forms.ModelChoiceField(
        queryset=Food.objects.values_list("food", flat=True).distinct(),
        empty_label=None
    )