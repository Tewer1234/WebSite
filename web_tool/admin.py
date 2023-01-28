from django.contrib import admin
from web_tool.models import Browsetable, MrnaTbl,Datatable,W285Table
# Register your models here.
class GeneAdmin(admin.ModelAdmin):
	list_display = ("numid","geneid", "transcriptid", "numbers")
	search_fields = ("geneid", "transcriptid")
	ordering = ("numid","geneid", "transcriptid", "numbers")  

class dataAdmin(admin.ModelAdmin):
    list_display = ("geneid","status","sequence","genename","othername")
    search_fields = ("geneid","status","sequence","genename","othername")
    ordering = ("geneid","status","sequence","genename","othername")

class tableAdmin(admin.ModelAdmin):
    list_display = ("geneid","status","sequence","genename","othername","transcript","type","transcript_count")
    search_fields = ("geneid","status","sequence","genename","othername","transcript","type","transcript_count")
    ordering = ("geneid","status","sequence","genename","othername","transcript","type","transcript_count")

class browseAdmin(admin.ModelAdmin):
    list_display = ("transcriptid","geneid","status","sequence","genename","othername","types")
    search_fields = ("transcriptid","geneid","status","sequence","genename","othername","types")
    ordering = ("transcriptid","geneid","status","sequence","genename","othername","types")

admin.site.register(MrnaTbl,GeneAdmin)
admin.site.register(Datatable,dataAdmin)
admin.site.register(W285Table,tableAdmin)
admin.site.register(Browsetable,browseAdmin)
