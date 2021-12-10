from django.contrib import admin
from .models import Produit
from .models import Ville
from .models import Partenaire
from .models import*
class AdminProduit(admin.ModelAdmin):
    list_display = ['commune', 'prix' , 'ville']
     

class AdminVille(admin.ModelAdmin):
    list_display = ['nom']
     
#Register your models here.

admin.site.register(Produit, AdminProduit)
admin.site.register(Ville, AdminVille)
#admin.site.register( Partenaire )
# admin.site.register( PubDet )
# admin.site.register( PubConnect )
# admin.site.register( PubCrecomp )
# admin.site.register( PubChangp )
# admin.site.register( PubAcc )
admin.site.register( Age )
admin.site.register( Commune )
admin.site.register( Plusdemande )