from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Profile, Skill


def paginate_profiles(request, profiles, results):

    page = request.GET.get('page')
    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    # in case user queries the page that don't exist, send user to the last page availible 
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    # for large range of numbers

    left_index = (int(page) - 4)
    right_index = (int(page) + 5)

    if left_index < 1:
        left_index = 1

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)
    return custom_range, profiles


def search_profiles(request):
    search_query = ''

    # implementng filter by quering the value of 'search_query' attribute from HTML
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    #  searching skills
    skills = Skill.objects.filter(name__iexact=search_query)

    # accessing the data from model
    # icontains ignores case
    # using filter method and importing Q from django models to implement search by several fields 
    profiles = Profile.objects.distinct().filter(
                                    Q(name__icontains=search_query)| 
                                    Q(short_intro=search_query) |
                                    Q(skill__in=skills)
                                )    
    return profiles, search_query

