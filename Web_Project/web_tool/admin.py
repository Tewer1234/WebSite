from django.contrib import admin
from web_tool.models import GeneTbl
# Register your models here.
class GeneAdmin(admin.ModelAdmin):
	list_display = ("numid","geneid", "transcriptid", "numbers")
	search_fields = ("geneid", "transcriptid")
	ordering = ("numid","geneid", "transcriptid", "numbers")  


admin.site.register(GeneTbl,GeneAdmin)
