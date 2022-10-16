from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView



from .forms import SearchForm
from .models import Course, Teacher

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

class TeacherDetailView(DetailView):
    model = Teacher


# class UserSignup(View):
#     def get(self, request):
#         context = {'form': UserCreationForm()}
#         return render(request, 'schedule/enroll.html', context)
#
#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('main')
#         else:
#             context = {'form': form}
#             return render(request, 'schedule/enroll.html', context)


class UserSignup(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('main')
    template_name = 'schedule/enroll.html'
