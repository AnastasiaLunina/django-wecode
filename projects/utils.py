from django.db.models import Q
from .models import Project, Tag

def search_projects(request):
    search_query = ''

    # implementng filter by quering the value of 'search_query' attribute from HTML
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.distinct().filter(name__icontains=search_query)


    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        # get the project where the owners name contains search_query
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )

    return projects, search_query
