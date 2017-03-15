from django.shortcuts import render
from django.template import loader
from .models import *

def index(request):
    # school = School.objects.order_by('name')
    # grade_list = Grade.objects.order_by('teacher')
    # children = Child.objects.order_by('last_name')
    # context = {
    # 'grade_list': grade_list,
    # 'children': children,
    # 'school': school,
    # }
    return render(request, 'CRM/index.html')#, context)



def schools(request):
    schools = KGardens.objects.order_by('name')
    example = KGardens.objects.get(id=201)
    context = {
        'schools':schools,
        'example':example,
    }
    return render(request, 'CRM/schools.html', context)

def classes(request):
    classes = Groups.objects.order_by('k_garden_id')
    return render(request, 'CRM/classes.html', {'classes': classes})

def classes_per_school(request, k_garden_id):
    school = KGardens.objects.get(id = k_garden_id)
    classes = Groups.objects.filter(k_garden_id = k_garden_id)
    context = {
        'classes': classes,
        'school': school,
    }
    return render(request, 'CRM/classes.html', context)

def children(request):
    children = Kids.objects.all()
    return render(request, 'CRM/children.html', {'children': children})


def gallery(request):
    pictures = KidPhotos.objects.order_by('updated_at')
    return render(request, 'CRM/gallery.html', {'pictures': pictures})

def gallery_per_kid(request):
    kid_pics = KidPhotos.objects.filter(kid_id = 685)
    kid = Kids.objects.get(id = 685)
    return render(request, 'CRM/kid_gallery.html', {'kid_pics': kid_pics, 'kid':kid})

def gallery_per_class(request):
    class_name = Groups.objects.get(id = 361)
    pics = KidPhotos.objects.all()
    return render(request, 'CRM/class_gallery.html', {'class': class_name, 'pics': pics})

def children_per_class(request, k_garden_id, group_id):
    school = KGardens.objects.get(id = k_garden_id)
    group = Groups.objects.get(id = group_id)
    children = Kids.objects.filter(group_id = group_id)
    context = {
        'school': school.name,
        'group': group.name,
        'children': children,
    }
    return render(request, 'CRM/children.html', context)

def reports(request):
    # children = Child.objects.order_by('last_name')
    return render(request, 'CRM/reports.html')#, {'children': children})

def staff(request):
    # staff = Staff.objects.order_by('first_name')
    return render(request, 'CRM/staff.html')#, {'staff': staff})

def attendances(request):
    # staff = Staff.objects.order_by('first_name')
    return render(request, 'CRM/attendances.html')#, {'staff': staff})

def contacts(request):
    # staff = Staff.objects.order_by('first_name')
    # school = KGardens.objects.get(id=k_garden_id)
    # group = Groups.objects.get(id=group_id)
    # children = Kids.objects.filter(group_id=group_id)
    # contacts = Contacts.objects.filter(kid_id=kid_id)
   #group = Groups.objects.get(id=group_id)
    #children = Kids.objects.filter(group_id=group_id)
    #contacts = Contacts.objects.filter(kid_id=kid_id)
    # context = {
    #     'school': school.name,
    #     'group': group.name,
    #     'children': children,
    #     'contacts': contacts,
    #
    # }
    return render(request, 'CRM/contactPerson.html')#, {'staff': staff})

def child_profile(request):
    return render(request,'CRM/child_profile.html')

def schools_view(request):

    return render(request, 'CRM/schools_view.html')