from django.shortcuts import render

# from AIDS.models import Student


# def students(request):
#     student = Student.objects.all()
#     context = {'student': student}
#     return render(request, 'student.html', context)




# from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

# class Forms(CreateView):
#     model = Student
#     fields = "__all__"
#     template_name = 'forms.html'
#     success_url = '/'

# class StudentList(ListView):
#     model = Student
#     template_name = 'stulist.html'

# class StudentDetail(DetailView):
#     model = Student
#     template_name = 'studetail.html'

# class StudentUpdate(UpdateView):
#     model = Student
#     fields = '__all__'
#     template_name = 'stuupdate.html'
#     success_url = '/'

# class StudentDelete(DeleteView):
#     model = Student
#     template_name = 'studelete.html'
#     success_url = '/'


# Create your views here.
def Home(request):
    return render(request, 'Home.html')

def products(request):
    return render(request, 'products.html')

def service(request):
    return render(request, 'service.html')

def contactus(request):
    return render(request, 'contactus.html')

def aboutus(request):
    return render(request, 'aboutus.html')