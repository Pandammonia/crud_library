from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from .models import Book, Author
from .forms import BookForm, AuthorForm

def index(request):
	request.session.set_test_cookie()
	if request.session.test_cookie_worked():
		print("Test worked!")
		request.session.delete_test_cookie()
	author = Author.objects.all()
	books = Book.objects.filter(status='available') #Only books with available set in admin are shown
	context = {'books':books, 'author':author}
	return render(request, 'library/index.html', context)

def sort(request):
	books = Book.objects.all()
	sort_by = request.POST.get('sort')
	if sort_by == 'genre':
		books = books.order_by('-genre')
		context = {'books':books}
		return HttpResponseRedirect(request, 'library/index.html', context)
	elif sort_by == 'author':
		books = books.order_by('-author')
		context = {'books':books}
		return HttpResponseRedirect(request, 'library/index.html', context)
	num = len(books)
	context = {'books':books, 'num':num}
	return render(request, 'library/index.html')

def addauthor(request):
	form = AuthorForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('library:index')
	else:
		form = AuthorForm()
	context = {'form':form}
	return render(request, "library/addauthor.html", context)

def addbook(request):
	form = BookForm(request.POST or None)
	if form.is_valid():
		form.save()
		instance = form.save()
		slug = instance.slug
		return redirect('library:detail', slug=slug)
	else:
		form = BookForm()
	context = {'form':form}
	return render(request, "library/addbook.html", context)

def bookdetails(request, slug):
	book = Book.objects.get(slug=slug)	
	context = {'book':book}
	return render(request, "library/detail.html", context)

def bookdelete(request, slug):
	book = get_object_or_404(Book, id=slug)
	if request.method == "POST":
		book.delete()
		return HttpResponseRedirect("/")
	context = {'book':book}
	return render(request, "library/bookdelete.html", context)

def bookupdate(request, slug):
	book = get_object_or_404(Book, id=slug)
	form = BookForm(request.POST or None, instance=book)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/"+id)
	context = {'form':form}
	return render(request, "library/bookupdate.html", context)

def authordetail(request, slug):
	author = Author.objects.get(id=slug)
	books = Book.objects.filter(author=slug)
	context = {'author':author, 'books':books}
	return render(request, "library/authordetail.html", context)

def search(request):
		return render(request, 'library/search.html')

def searchresults(request):
	if request.method == "POST":
		search_term = request.POST.get('search_term', None)
		try:
			results = Book.objects.filter(title=search_term)
			context = {'results': results}
			return render(request, 'library/searchresults.html', context)
		except BookDoesNotExist:
						return HttpResponse("No book with that title!")	
	else:
		return HttpResponse("Error")