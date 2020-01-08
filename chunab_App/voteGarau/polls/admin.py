from django.contrib import admin

# Register your models here.
from .models import Question,Choice

admin.site.site_header = "VoteGarau Admin"
admin.site.site_title = "Polls Admin Area"
admin.site.index_title = "Namaskar sabailai Polls admin area ma swagat xa"

class ChoiceInline(admin.TabularInline): 
    model = Choice  #defingn with whicl class to work with frmmodels
    extra = 3    # how mny extra fields do we want


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),  #(names, {fields to display,'classes':[to display behaviours of field]}, )
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline] # to display the class choiceline data members in admin


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin) #register Question class using modeladmin fetaures