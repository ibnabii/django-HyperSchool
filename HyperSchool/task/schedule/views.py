from django.shortcuts import render
from django.views.generic.detail import DetailView

from .forms import SearchForm
from .models import Course

def main(request):
    form = SearchForm(request.GET)

    queryset = Course.objects

    if form.is_valid():
        q = form.cleaned_data.get('q', '').strip()
        queryset = queryset.filter(title__icontains=q)

    context = {
        'courses': queryset.all(),
        'form': form
    }

    return render(request, 'schedule/main.html', context=context)


class CourseDetailView(DetailView):
    model = Course
