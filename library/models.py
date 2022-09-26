from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Author(models.Model):
	name = models.CharField(max_length=100)
	age = models.DecimalField(decimal_places=0, max_digits=3)

	def __str__(self):
		return self.name


class Book(models.Model):

	genre_choice = [
	('Horror', 'Horror'),
	('Romance', 'Romance'),
	('Sci-fi', 'Sci-fi'),
	('Adventure', 'Adventure'),
	('None-fiction', 'None-fiction'),
	('Drama', 'Drama'),
	('History', 'History'),
	('Science', 'Science'),
	('Technology', 'Technology'),
	('Art', 'Art'),
	('Autobiography', 'Autobiography'),
	('Other', 'Other'),
	]

	status = [
	('available', 'Available'),
	('not available', 'Not available'),
	]

	title = models.CharField(max_length=100)
	written = models.DecimalField(max_digits=4, decimal_places=0)
	genre = models.CharField(max_length=25, choices=genre_choice)
	added = models.DateTimeField(auto_now_add=True)
	edited = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=20, choices=status)
	author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
	description = models.TextField(null = True)
	slug = models.SlugField(null=True)
	price = models.DecimalField(max_digits=4, decimal_places=2, null=True)

	def get_absolute_url(self):
		return reverse("library:detail", kwargs={'slug' : self.slug })

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)

	def __str__(self):
		return self.title