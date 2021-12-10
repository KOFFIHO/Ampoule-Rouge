from django.shortcuts import render, redirect
from .forms import CreateUserForm 
from .forms import ProduitForm 
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import query
from django.contrib.sites.shortcuts import get_current_site
# # Create your views here.

def index(request):
    plusdemandes = Plusdemande.objects.all()
    pubAccs = PubAcc.objects.all()
    produits = None
    plusdemandes = Plusdemande.get_all_plusdemandes()
    communes = Commune.get_all_communes()
    communeID = request.GET.get('commune')
    ages = Age.get_all_ages()
    ageID = request.GET.get('age')
    villes = Ville.get_all_villes()
    villeID = request.GET.get('ville')
    if villeID:
        produits = Produit.objects.filter(ville=villeID)
    else:
        produits = Produit.objects.all().order_by('date_ajout').reverse()
    data = {}
    data['plusdemandes'] = plusdemandes
    data['pubAccs'] = pubAccs
    data['produits'] = produits
    data['villes'] = villes
    data['communes'] = communes
    data['ages'] = ages
    return render(request,'index.html',data)

def boutique(request):
    return render(request,'boutique.html')

def rechercheform(request):
    #nombre=0
    communes = Commune.get_all_communes()
    ages = Age.get_all_ages()
    villes = Ville.get_all_villes()
    message = ""
    query = request.GET.get('query')
    age =request.GET.get('age')
    commune =request.GET.get('commune')
    ville=request.GET.get('ville')
    if not query:
        if ville == "0" and age=="0" and commune=="0":
            produits = Produit.objects.all()
        elif ville != "0" and age=="0" and commune=="0":
            produits = Produit.objects.filter(ville_id=ville)

        elif ville != "0" and age !="0" and commune=="0":
                produits = Produit.objects.filter(ville_id=ville,age_id=age)

        elif ville != "0" and age !="0" and commune !="0":
                produits = Produit.objects.filter(ville_id=ville,age_id=age,commune_id=commune)

        elif ville == "0" and age !="0" and commune =="0":
                produits = Produit.objects.filter(age_id=age)

        elif ville == "0" and age !="0" and commune !="0":
                produits = Produit.objects.filter(age_id=age,commune_id=commune)
        
        elif ville != "0" and age =="0" and commune !="0":
                produits = Produit.objects.filter(ville_id=ville,commune_id=commune)

        elif ville == "0" and age !="0" and commune =="0":
                produits = Produit.objects.filter(age_id=age)
        
        elif ville == "0" and age =="0" and commune !="0":
                produits = Produit.objects.filter(commune_id=commune)
        
        #elif ville != "0" and age !="0" and commune =="0":
        #        produits = Produit.objects.filter(ville_id=ville,age_id=age)
        else:
            produits = Produit.objects.all()

    else:
        # title contains the query and query is not sensitive to case.
        if ville == "0" and age=="0" and commune=="0":
            produits = Produit.objects.filter(quartier__icontains=query)
            if not produits.exists():
                produits = Produit.objects.filter(taille__icontains=query) 
            if not produits.exists():
                produits = Produit.objects.filter(prix__icontains=query)  
            if not produits.exists() :
                message ="Aucun resulat trouvé pour %s"%query
                context = {
                    'message':message
                    }
        else:
            produits = Produit.objects.filter(quartier__icontains=query,ville_id=ville)
            if not produits.exists():
                produits = Produit.objects.filter(taille__icontains=query,ville_id=ville) 
            if not produits.exists():
                produits = Produit.objects.filter(prix__icontains=query,ville_id=ville)

            if not produits.exists():
                produits = Produit.objects.filter(quartier__icontains=query,commune_id=commune)
            if not produits.exists():
                produits = Produit.objects.filter(taille__icontains=query,commune_id=commune) 
            if not produits.exists():
                produits = Produit.objects.filter(prix__icontains=query,commune_id=commune)
            
            if not produits.exists():
                produits = Produit.objects.filter(quartier__icontains=query,age_id=age)
            if not produits.exists():
                produits = Produit.objects.filter(taille__icontains=query,age_id=age) 
            if not produits.exists():
                produits = Produit.objects.filter(prix__icontains=query,age_id=age)

            if not produits.exists() :
                message ="Aucun resulat trouvé pour %s"%query 
                context = {
                    'message':message
                    }

    context = {
        'produits':produits,
        'message':message,
        'villes':villes,
        'communes' :communes,
        'ages': ages
    }
    return render(request, 'index.html',context)


def details(request ,slug):
    produit = Produit.objects.get(slug=slug)
    pubDets = PubDet.objects.all()
    communes = Commune.objects.all()
    partenaire=Partenaire.objects.all()
    current_site = get_current_site(request)
    message = "NOUVELLE DEMANDE : salut,je suis interressé par votre produit "+ produit.commune.nom+ " http://"+str(current_site)
    
    context={
        'communes': communes,
        'pubDets': pubDets,
        'produit':produit,
        'partenaire':partenaire,
        'message':message
        }
    return render(request, 'details.html',context)

def detailsnew(request ,detailsnew_id):
    id= int(detailsnew_id)
    plusdemande = Plusdemande.objects.get(id=detailsnew_id)
    pubDets = PubDet.objects.all()
    communes = Commune.objects.all()
    partenaire=Partenaire.objects.all()
    current_site = get_current_site(request)
    message = "NOUVELLE DEMANDE : salut,je suis interressé par votre produit "+ plusdemande.commune.nom+ " http://"+str(current_site)
    
    context={
        'communes': communes,
        'pubDets': pubDets,
        'plusdemande':plusdemande,
        'partenaire':partenaire,
        'message':message
    }
    return render(request, 'detailsnew.html',context)

def register(request):
    pubCrecomps = PubCrecomp.objects.all()
    form = CreateUserForm()
    if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Votre compte a été créé '+ user)

                return redirect('loginPage')

    context={
        'form':form,
        'pubCrecomps':pubCrecomps,
    }
    return render(request, 'account/register.html', context) 

def loginPage(request):
    pubConnects = PubConnect.objects.all()
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  
            return redirect('index') 
        else:
            messages.info(request, 'Username, password est incorrect')
    context={ 
        'pubConnects':pubConnects
    }
    return render(request, 'account/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('loginPage') 

def register(request):
    pubCrecomps = PubCrecomp.objects.all()
    form = CreateUserForm()
    if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Votre compte a été créé '+ user)

                return redirect('loginPage')

    context={
        'form':form,
        'pubCrecomps':pubCrecomps,
        }
    return render(request, 'account/register.html', context) 

@login_required(login_url="loginPage")
def ajoutimmoPage(request):
    communes = Commune.objects.all()
    pubChangps = PubChangp.objects.all()
    villes = Ville.objects.all()
    ages = Age.objects.all()
    form = ProduitForm()
    #form = ProduitForm(data=(request.POST or None),instance=produits)
    if request.method == 'POST':
        form = ProduitForm(request.POST,request.FILES)
        commune=request.POST.get("commune") # recuperer une valeur foreignkey
        ville=request.POST.get("ville")
        age=request.POST.get("age")
        if form.is_valid():
            form = form.save(commit=False)
            form.commune.id= commune
            form.ville.id= ville
            form.age.id= age
            form.save()
            message="VOTRE PRODUIT A ETE AJOUTER ."
            return redirect('index')
        else:
            print(form.errors) 
            error="ok"
            form = ProduitForm() 

    context={
        'pubChangps': pubChangps,
        'ages' : ages,
        'communes': communes,
        'villes' : villes,
        'form': form,
        }
    return render(request, 'ajoutimmo.html',context)

def passwordchange(request):
    pubChangps = PubChangp.objects.all()
    message=""
    context={ 'pubChangps': pubChangps,}
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        conf_password=request.POST.get("conf_password")
        if password==conf_password:
            try:
                user=User.objects.get(username=username)
                user.set_password(password)
                user.save()
                return redirect('loginPage')
            except:
                message=" L'utilisateur "  + username +  " n'existe pas"
        else:
            message="Veuillez saisir des mots de passe identiques"
        context={
            'message':message,
            'pubChangps': pubChangps,
        }
    return render(request, 'account/passwordchange.html', context)
    
