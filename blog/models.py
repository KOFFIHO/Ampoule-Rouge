from django.db import models
from django.urls import reverse

# Create your models here.
class Ville(models.Model):
    nom = models.CharField(max_length=100)
    
    @staticmethod
    def get_all_villes():
        return Ville.objects.all()

    def __str__(self):
        return self.nom

class Commune(models.Model):
    nom = models.CharField(max_length=100)
    
    @staticmethod
    def get_all_communes():
        return Commune.objects.all()

    def __str__(self):
        return self.nom

class Age(models.Model):
    nom = models.CharField(max_length=100)
    
    @staticmethod
    def get_all_ages():
        return Age.objects.all()

    def __str__(self):
        return self.nom

class Partenaire(models.Model):
    nomPart = models.CharField(max_length=200)
    logoPart = models.ImageField(upload_to='partenaire')

    @staticmethod
    def get_all_partenaires():
        return Partenaire.objects.all()

    def __str__(self):
        return self.nomPart

class Produit(models.Model):
    nom = models.CharField(max_length=20)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    prix = models.IntegerField()
    date_ajout=models.DateTimeField(auto_now_add=True)
    numero=models.CharField(max_length=20)
    slug=models.CharField(max_length=50)
    age = models.ForeignKey(Age, on_delete=models.CASCADE)
    taille = models.FloatField()
    tein = models.CharField(max_length=100 ,blank=True,null=True)
    forme = models.CharField(max_length=100 ,blank=True,null=True)
    quartier = models.CharField(max_length=100 ,blank=True,null=True)
    image1 = models.ImageField(upload_to='img/maison')
    image2 =models.ImageField(upload_to='img/maison')
    image3 =models.ImageField(upload_to='img/maison',blank=True,null=True)
    image4 =models.ImageField(upload_to='img/maison',blank=True,null=True)
    image5 =models.ImageField(upload_to='img/maison',blank=True,null=True)
    #superficie = models.IntegerField(blank=True,null=True)
    #couleurExt=models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True)

    def register(self):
            self.save()

    @staticmethod
    def get_all_prodtuits():
        return Produit.objects.all()    

    @staticmethod
    def get_all_prodtuits_by_produitid(ville_id):
        if ville_id:
            return Produit.objects.filter(ville = ville_id)
        else:
            return Produit.get_all_prodtuits()

    def get_absolute_url(self):
        return reverse('details',slug=[str(self.slug)])


class PubAcc(models.Model):
    pub1 = models.FileField(upload_to='puba')
    nonEntrep = models.CharField(max_length=50 ,blank=True,null=True) 
    messag1 = models.CharField(max_length=700,blank=True,null=True)
    messag2 = models.CharField(max_length=700,blank=True,null=True)
    lien =  models.CharField(max_length=100,blank=True,null=True)
    
    # def __str__(self):
    #     return self.nonEntrep
    

class PubDet(models.Model):
    pub2 = models.FileField(upload_to='pubd')
    lien =  models.CharField(max_length=100,blank=True,null=True)

    # def __str__(self):
    #     return self.lien

class PubConnect(models.Model):
    pub3 = models.FileField(upload_to='pubcon')
    lien =  models.CharField(max_length=100,blank=True,null=True)

    # def __str__(self):
    #     return self.lien

class PubCrecomp(models.Model):
    pub4 = models.FileField(upload_to='pubcc')
    lien =  models.CharField(max_length=100,blank=True,null=True)

    # def __str__(self):
    #     return self.lien

class PubChangp(models.Model):
    pub5 = models.FileField(upload_to='pubchan')
    lien =  models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.lien

class Plusdemande(models.Model):
    nom = models.CharField(max_length=20)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    prix = models.IntegerField()
    date_ajout=models.DateTimeField(auto_now_add=True)
    numero=models.CharField(max_length=20)
    age = models.ForeignKey(Age, on_delete=models.CASCADE)
    taille = models.FloatField()
    tein = models.CharField(max_length=100 ,blank=True,null=True)
    forme = models.CharField(max_length=100 ,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    quartier = models.CharField(max_length=100 ,blank=True,null=True)
    image1 = models.ImageField(upload_to='img/maison')
    image2 =models.ImageField(upload_to='img/maison')
    image3 =models.ImageField(upload_to='img/maison',blank=True,null=True)
    image4 =models.ImageField(upload_to='img/maison',blank=True,null=True)
    image5 =models.ImageField(upload_to='img/maison',blank=True,null=True)

    def register(self):
            self.save()

    @staticmethod
    def get_all_plusdemandes():
        return Plusdemande.objects.all()    

    # # @staticmethod
    # # def get_all_plusdemandes_by_plusdemandeid(ville_id):
    # #     if ville_id:
    # #         return Plusdemande.objects.filter(ville = ville_id)
    # #     else:
    # #         return Plusdemande.get_all_plusdemandes()

    def get_absolute_url(self):
        return reverse('detailsnew',slug=[str(self.slug)])