from django.contrib import admin

# Register your models here.
from Caracteristqiue.models import Utilite,Pam,Avoir
class PamAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Nom_scientifique',)}

admin.site.register(Utilite)
admin.site.register(Pam,PamAdmin)
admin.site.register(Avoir)
