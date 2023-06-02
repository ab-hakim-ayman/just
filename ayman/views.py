from django.shortcuts import render, redirect
from math import ceil

from . models import(
    About, Skill, Social, Education,
    Experience, Service, Project, Category,
    Testimonial, Contact, Achievement
)
from .forms import ContactForm

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
    category = Category.objects.filter(is_active=True)
    testimonials = Testimonial.objects.all()
    achievements = Achievement.objects.filter(is_active=True)
    context = {
        'abouts':abouts,
        'left_skills':left_skills,
        'right_skills':right_skills,
        'educations':educations,
        'socials':socials,
        'experiences':experiences,
        'services':services,
        'projects':projects,
        'category':category,
        'testimonials':testimonials,
        'achievements':achievements,
    }
    return render(request, 'home.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email'),
                subject=form.cleaned_data.get('subject'),
                message=form.cleaned_data.get('message')
            )
        return redirect(home)