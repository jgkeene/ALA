from django.shortcuts import render
from .models import Reddit, Slashdot, Hackernews

def index(request):
    num_records=Reddit.objects.all().count()
    return render(
        request,
        'index.html',
        context={ 'num_records':num_records, },
    )

from django.views import generic
class RedditListView(generic.ListView):
    model = Reddit
#    dates = Reddit.objects.all().distinct('date')
    dates = Reddit.objects.all().count()


#    context_object_name = 'my_book_list'   # your own name for the list as a template variable
#    queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
#    template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location

    #paginate_by = 20


class SlashdotListView(generic.ListView):
    model = Slashdot
    #paginate_by = 20

class HackernewsListView(generic.ListView):
    model = Hackernews
    #paginate_by = 20



