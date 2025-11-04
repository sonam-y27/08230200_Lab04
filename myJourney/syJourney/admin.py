from django.contrib import admin
from .models import (
    Skill,
    LearningExperience,
    Challenge,
    Reflection,
    Hobby,
    Strength,
    Weakness
)

# =======================
# Admin registration
# =======================

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(LearningExperience)
class LearningExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    ordering = ('order',)
    search_fields = ('title',)

@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Reflection)
class ReflectionAdmin(admin.ModelAdmin):
    list_display = ('id',)
    ordering = ('id',)

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Strength)
class StrengthAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Weakness)
class WeaknessAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
