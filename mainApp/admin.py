from django.contrib import admin
from .models import *


class KitobInline(admin.StackedInline):
    model = Kitob
    extra = 1


class MuallifAdmin(admin.ModelAdmin):
    list_display = ['ism', 'davlat', 'kitob_soni', 'tirik']
    list_display_links = ['ism']
    list_filter = ['tirik']
    search_fields = ['ism']
    date_hierarchy = 't_sana'
    list_editable = ['kitob_soni', 'tirik']
    inlines = [KitobInline]


class KitobAdmin(admin.ModelAdmin):
    list_display = ['nom', 'janr', 'muallif', 'sahifa']
    list_display_links = ['nom', 'muallif']
    list_filter = ['muallif', 'janr']
    list_editable = ['sahifa']
    list_per_page = 4
    search_fields = ['nom', 'janr']


class KutubxonachiAdmin(admin.ModelAdmin):
    list_display = ['ism', 'ish_vaqti']
    list_display_links = ['ism']
    list_filter = ['ish_vaqti']
    search_fields = ['ism']



class TalabaAdmin(admin.ModelAdmin):
    list_display = ["ism", "kurs", "guruh", "yosh", "kitob_soni"]
    list_display_links = ['ism']
    list_filter = ['kurs', 'yosh', 'kitob_soni']
    list_editable = ['kurs', 'kitob_soni']
    search_fields = ['ism', 'kurs', 'guruh', 'yosh', 'kitob_soni']

class RecordAdmin(admin.ModelAdmin):
    list_display = ["talaba","kitob","kutubxonachi", "qaytardi"]
    list_display_links = ['talaba', 'kutubxonachi', 'kitob']
    list_filter = ['talaba', 'kitob', 'kutubxonachi']



admin.site.register(Kitob, KitobAdmin)
admin.site.register(Muallif, MuallifAdmin)
admin.site.register(Talaba, TalabaAdmin)
admin.site.register(Kutubxonachi, KutubxonachiAdmin)
admin.site.register(Record, RecordAdmin)

