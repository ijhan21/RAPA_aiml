from django.contrib import admin
from polls.models import Question, Choice
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5

class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     ('Question Statement', {'fields':['question_text']}),
    #     ('Date Information', {'fields':['pub_date']}),
    #     ]
    fieldsets = [
        ('Question Statement', {'fields':['question_text']}),
        ('Date Information', {'fields':['pub_date'],'classes':['collapse']}),
        ]
    inlines = [(ChoiceInline)]
    list_display = ('question_text', 'pub_date')
    search_fields = ['question_text']



# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)