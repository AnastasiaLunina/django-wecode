from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Project, Tag


def paginate_projects(request, projects, results):

    page = request.GET.get('page')
    # results = 4
    paginator = Paginator(projects, results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    # in case user queries the page that don't exist, send user to the last page availible 
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    # for large range of numbers

    left_index = (int(page) - 4)
    right_index = (int(page) + 5)

    if left_index < 1:
        left_index = 1

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)
    return custom_range, projects

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
