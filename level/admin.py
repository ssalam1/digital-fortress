from level.models import level
from django.contrib import admin

class levelAdmin(admin.ModelAdmin):
	list_diplay = ('max_level','email')
		

	
admin.site.register(level,levelAdmin)
