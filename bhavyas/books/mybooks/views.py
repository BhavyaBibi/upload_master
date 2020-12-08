from django.http import HttpResponse
from django.shortcuts import render,render_to_response, get_object_or_404
from mybooks.models import books
from mybooks.forms import booksform
def home(request):
    return HttpResponse("Welcome")
def bookie(request):
	b=books.objects.all()
	return render(request,'bookie.html',{'bookie':b})

def upload(request):
    form=booksform()
    if(request.method=='POST'):
        form=booksform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return bookie(request)
    return render(request,'upload.html',{'form':form})


def delete_book(request, pk):
    b = books.objects.get(pk=pk)
    b.delete()

    return bookie(request)


def view_book(request, pk):
    instance = get_object_or_404(books, pk=pk)

    context = {
        'instance': instance,

    }
    return render(request, 'view.html', context)


def edit_book(request, pk):
    e=books.objects.get(pk=pk)
    form = booksform(instance=e)
    if (request.method == 'POST'):
        form = booksform(request.POST, request.FILES,instance=e)
        if (form.is_valid()):
            form.save()
            return bookie(request)
    return render(request, 'upload.html', {'form': form})
def setsession(request):
    request.session['username']='sanjay'
    return HttpResponse('hello')
def getsession(request):
    p=request.session['username']
    return render(request,'user.html',{'p':p})



