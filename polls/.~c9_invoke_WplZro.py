from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
	#Variables
	model=	Choice
	extra=	3
## End of ChoiceInline

class QuestionAdmin(admin.ModelAdmin):
	# Variables
	fieldsets=  [
		(None,	{
			"fields":	["question_text"]
		}),
		("Date information",	{
			"fields":	["pub_date"]
		})
	]
	inlines=	[ChoiceInline]
## End of QuestionAdmin

admin.site.register(Question, QuestionAdmin)