from django.contrib import admin
from .models import Autorius, Zanras, Knyga, KnygosKopija

class KnygosKopijaAdmin(admin.ModelAdmin):
    list_display = ('knyga', 'statusas', 'grazinama')
    list_editable = ('grazinama', 'statusas')
    list_filter = ('statusas', 'grazinama')
    search_fields = ('uuid', 'knyga__pavadinimas')

    fieldsets = (
        ('Bendra', {'fields': ('uuid', 'knyga')}),
        ('Prieinamumas', {'fields': ('statusas', 'grazinama')}),
    )
class KnygosKopijaInline(admin.TabularInline):
    model = KnygosKopija
    extra = 0
    readonly_fields = ('uuid',)
    can_delete = False

class KnygaAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'autorius', 'parodyti_zanra')
    inlines = [KnygosKopijaInline]

class AutoriusAdmin(admin.ModelAdmin):
    list_display = ('autoriaus_v', 'autoriaus_p', 'parodyti_knygas')




admin.site.register(Knyga, KnygaAdmin)
admin.site.register(Autorius, AutoriusAdmin)
admin.site.register(Zanras)
admin.site.register(KnygosKopija, KnygosKopijaAdmin)
