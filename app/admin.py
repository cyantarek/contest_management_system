from django.contrib import admin
from . import models

# Register your models here.

class QuestionInline(admin.StackedInline):
	model = models.Question
	extra = 2

class ContestAdmin(admin.ModelAdmin):
	model = models.Contest
	inlines = [QuestionInline]

admin.site.register(models.Contest, ContestAdmin)
admin.site.register(models.Member)
admin.site.register(models.Question)
admin.site.register(models.Solution)
