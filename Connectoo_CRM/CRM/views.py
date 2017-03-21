from django.shortcuts import render, redirect
from django.template import loader
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
def index(request):
    school = KGardens.objects.get(id=201)
    group = Groups.objects.order_by('name')
    children = Kids.objects.order_by('last_name')
    context = {
    'group': group,
    'children': children,
    'school': school,
    }
    return render(request, 'CRM/index.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Connectoo').exists(), login_url='/')
def schools_table(request):
    schools = KGardens.objects.get(id=201)
    context = {
        'schools':schools
    }
    return render(request, 'CRM/schools_table.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Manager').exists(), login_url='/')
def classes_table(request):
    # classes = Groups.objects.order_by('k_garden')
    school = KGardens.objects.get(id = 201)
    classes = Groups.objects.filter(k_garden_id = 201)
    context = {
        'school':school,
        'classes':classes
    }
    return render(request, 'CRM/classes_table.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Manager').exists(), login_url='/')
def classes_per_school(request, k_garden_id):
    school = KGardens.objects.get(id = k_garden_id)
    classes = Groups.objects.filter(k_garden_id = k_garden_id)
    context = {
        'classes': classes,
        'school': school,
    }
    return render(request, 'CRM/classes.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Manager').exists(), login_url='/')
def children_per_school(request, k_garden_id):
    school = KGardens.objects.get(id = k_garden_id)
    classes = Groups.objects.filter(k_garden_id = k_garden_id)
    context = {
        'school': school,
        'group':classes,
    }
    return render(request, 'CRM/children_per_school.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Connectoo').exists(), login_url='/')
def gallery(request):
    pictures = KidPhotos.objects.order_by('updated_at')
    return render(request, 'CRM/gallery.html', {'pictures': pictures})


@login_required
def gallery_kid(request, kid_id):
    kid_pics = KidPhotos.objects.filter(kid_id = kid_id)
    tagged_pics = Tags.objects.filter(kid_id = kid_id)[:20]
    kid = Kids.objects.get(id = kid_id)
    context = {
        'kid_pics': kid_pics,
        'kid':kid,
        'tagged_pics':tagged_pics
        }
    return render(request, 'CRM/gallery_kid.html', context)


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Teacher').exists(), login_url='/')
def gallery_class(request, group_id):
    kids = Kids.objects.filter(group_id = group_id)
    group = Groups.objects.get(id = group_id)
    context = {
        'kids': kids,
        'group': group
        }
    return render(request, 'CRM/gallery_class.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Teacher').exists(), login_url='/')
def gallery_schools(request, k_garden_id):
    groups = Groups.objects.filter(k_garden = 201)
    school = KGardens.objects.get(id = k_garden_id)
    # kids = Kids.objects.filter(group_id = group.id)
    context = {
        'groups': groups,
        'school': school,
    }
    return render(request, 'CRM/gallery_schools.html', context)


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Teacher').exists(), login_url='/')
def children_per_class(request, group_id):
    group = Groups.objects.get(id = group_id)
    children = Kids.objects.filter(group_id = group_id)
    context = {
        'group': group,
        'children': children,
    }
    return render(request, 'CRM/children_per_class.html', context)


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Connectoo').exists(), login_url='/')
def schools(request):
    schools = KGardens.objects.order_by('name')
    example = KGardens.objects.get(id=201)
    context = {
        'schools':schools,
        'example':example,
    }
    return render(request, 'CRM/schools.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Teacher').exists(), login_url='/')
def reports(request):
    # children = Child.objects.order_by('last_name')
    return render(request, 'CRM/reports.html')#, {'children': children})


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Manager').exists(), login_url='/')
def staff(request):
    # staffs = Users.objects.filter(k_garden_id = 201).filter(profile = 1)
    staffs = Users.objects.filter(k_garden_id = 201).filter(profile = 1)
    school = KGardens.objects.get(id = 201)
    context = {
        'staffs':staffs,
        'school':school,
    }
    return render(request, 'CRM/staff.html', context)



@login_required
@user_passes_test(lambda u: u.groups.filter(name='Teacher').exists(), login_url='/')
def attendances(request):
    attendance = KidPresences.objects.order_by('first_name')
    return render(request, 'CRM/attendances.html')#, {'staff': staff})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Teacher').exists(), login_url='/')
def contacts(request, k_garden_id):
    # contacts = Contacts.objects.all()[:30]

    school = KGardens.objects.get(id = k_garden_id)
    classes = Groups.objects.filter(k_garden_id = k_garden_id)
    context = {
        'school': school,
        'group': classes,
    }
    return render(request, 'CRM/contacts.html', context)


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Teacher').exists(), login_url='/')
def child_profile(request, kid_id):
    kid = Kids.objects.get(id = kid_id)
    contacts = Contacts.objects.filter(kid=kid_id)
    context = {
        'kid': kid,
        'contacts': contacts,
    }
    return render(request,'CRM/child_profile.html', context)


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Teacher').exists(), login_url='/')
def child_profile_health(request, kid_id):
    kid = Kids.objects.get(id = kid_id)
    context = {
        'kid': kid
    }
    return render(request, 'CRM/child_profile_health.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Teacher').exists(), login_url='/')
def child_profile_reports(request, kid_id):
    reports = Agendas.objects.filter(agendable_id = kid_id)
    sleeps = Sleeps.objects.filter(kid_id = kid_id).order_by('-updated_at')
    kid = Kids.objects.get(id = kid_id)
    # attendances = KidPresences.objects.filter(kid_id = kid_id).order_by('-updated_at')
    context = {
        'kid': kid,
        'attendances': attendances,
        'reports': reports,
        'sleeps': sleeps,
    }
    return render(request, 'CRM/child_profile_reports.html', context)


def add_to_album(request):
    return render(request, 'CRM/add_to_album.html')

def staff_table(request):
    return render(request, 'CRM/staff_table.html')

def calendar(request):
    return render(request, 'CRM/calendar.html')

def magnet(request, group_id):
    children = Kids.objects.filter(group_id=group_id)
    # contacts = Contacts.objects.filter(kid_id=kid_id)
    staffs = Users.objects.filter(k_garden_id=201).filter(profile=1)
    context = {
        'children': children,
        'contacts': contacts,
        'staffs': staffs,
    }
    return render(request, 'CRM/magnet.html',context)

def album(request):
    return render(request, 'CRM/my_album.html')

