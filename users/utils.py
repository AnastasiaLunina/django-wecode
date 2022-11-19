from django.db.models import Q
from .models import Profile, Skill

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

