from django.shortcuts import render
from math import ceil

from . models import(
    About, Skill, Social, Education,
    Experience, Service, Project,
    Testimonial, Contact
)

# Create your views here.
def home(request):
    abouts = About.objects.filter(is_active=True)
    skills = Skill.objects.all().count()
    left_skills = Skill.objects.filter(is_active=True)[:int(skills/2)]
    right_skills = Skill.objects.filter(is_active=True)[int(skills/2):skills]
    educations = Education.objects.filter(is_active=True)
    socials = Social.objects.filter(is_active=True)
    experiences = Experience.objects.filter(is_active=True)
    services = Service.objects.filter(is_active=True)
    projects = Project.objects.filter(is_active=True)
    testimonials = Testimonial.objects.all()
    context = {
        'abouts':abouts,
        'left_skills':left_skills,
        'right_skills':right_skills,
        'educations':educations,
        'socials':socials,
        'experiences':experiences,
        'services':services,
        'projects':projects,
        'testimonials':testimonials,
    }
    return render(request, 'home.html', context)