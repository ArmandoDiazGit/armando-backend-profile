from django.contrib import admin
from .models import PersonalInfo, Bio, Skill, TimelineItem, CodeQuote, Project


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "email"]


@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Bio.objects.exists():
            return False
        return True


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "level", "category"]
    list_filter = ["category"]


@admin.register(TimelineItem)
class TimelineItemAdmin(admin.ModelAdmin):
    list_display = ["year", "title", "order"]
    list_editable = ["order"]


@admin.register(CodeQuote)
class CodeQuoteAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if CodeQuote.objects.exists():
            return False
        return True


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "code_url"]
