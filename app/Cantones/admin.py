from django.contrib import admin
from app.Cantones.models import Cantones

class AdminCantones(admin.ModelAdmin):

    list_display = ["codigo","nombre", "latitud", "longitud", "descripcion", "imagen"]
    list_editable = ["nombre", "latitud", "longitud", "descripcion", "imagen"]
    list_filter = ["codigo","nombre", "latitud", "longitud", "descripcion", "imagen"]
    search_fields = ["codigo", "nombre"]

    class Meta:
        model = Cantones

admin.site.register(Cantones, AdminCantones)
