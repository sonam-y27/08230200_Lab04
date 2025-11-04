from django.shortcuts import render
from .models import Skill, LearningExperience, Challenge, Reflection, Hobby, Strength, Weakness

def index(request):
    skills = Skill.objects.all()
    experiences = LearningExperience.objects.all()
    challenges = Challenge.objects.all()
    reflections = Reflection.objects.all()
    return render(request, 'index.html', {
        'skills': skills,
        'experiences': experiences,
        'challenges': challenges,
        'reflections': reflections
    })

def about_me(request):
    hobbies = Hobby.objects.all()
    strengths = Strength.objects.all()
    weaknesses = Weakness.objects.all()
    return render(request, 'aboutMe.html', {
        'hobbies': hobbies,
        'strengths': strengths,
        'weaknesses': weaknesses
    })
