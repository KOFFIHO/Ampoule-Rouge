from django.forms import ModelForm, TextInput, EmailInput,Textarea,DateInput
from django.forms import ModelForm,Form
from .models import *
from .models import Produit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class AgeForm(ModelForm):
    class Meta:
        model = Age
        fields = ['nom']

class CommuneForm(ModelForm):
    class Meta:
        model = Commune
        fields = ['nom']


class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = ['commune','ville','prix','numero','slug','age','taille','description','quartier','image1','image2','image3','image4','image5']
        widgets = {
            'commune': TextInput(attrs={'placeholder':' Commune ?','class':'form-control'}),
            'ville': TextInput(attrs={'placeholder':'Quel est la ville ?'}),
            'prix': TextInput(attrs={'placeholder':'Quel est prix ?'}),
            'numero': TextInput(attrs={'placeholder':'225 XX XX XX XX XX'}),
            'slug': TextInput(attrs={'placeholder':'exep(koffi_honore_ndri1)'}),
            'age': TextInput(attrs={'placeholder':'Exp(LOCATION, EN VENTE) ?'}),
            'taille': TextInput(attrs={'placeholder':'Taille ?'}),
            'quartier': TextInput(attrs={'placeholder':'Quel quartier ?'}), 
            'description': TextInput(attrs={'placeholder':' Description ?'}),
            #'superficie': TextInput(attrs={'placeholder':'Quel est la superficie(600) ?','class':'form-control-lg'}),
            #'couleurExt': TextInput(attrs={'placeholder':'Quelle est la couleur Exterieur ?', 'class':'datepicker form-control-lg'}),
            #'couleurInte': TextInput(attrs={'class': 'form-control','placeholder':'Quelle est la couleur interieur'})
        }
 