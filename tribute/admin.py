from django.contrib import admin
from .models import Obituary

class ObituaryAdmin(admin.ModelAdmin):

    list_display = ('name', 'date_of_birth', 'date_of_death', 'submission_date', 'author', 'slug')
    

    search_fields = ('name', 'author', 'content')
    
  
    list_filter = ('date_of_birth', 'date_of_death', 'submission_date')
    

    prepopulated_fields = {"slug": ("name",)}
    
  
    ordering = ('-submission_date',)  # Orders by submission date in descending order

# Register the Obituary model with custom admin settings
admin.site.register(Obituary, ObituaryAdmin)
