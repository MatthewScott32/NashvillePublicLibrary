from django.urls import include, path
from .views import *
from django.urls import path


app_name = "libraryapp"

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    path('librarians/', librarian_list, name='librarians'),
    path('library/', library_list, name='libraries'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('book/form', book_form, name='book_form'),
    path('librarian/form', librarian_form, name='librarian_form'),
    path('library/form', library_form, name='library_form'),
    path('books/<int:book_id>/', book_details, name='book'),
    path('librarian/<int:librarian_id>/', librarian_details, name='librarian'),
    path('library/<int:library_id>/', library_details, name='library'),
    path('books/<int:book_id>/form/', book_edit_form, name='book_edit_form'),
    path('librarian/<int:librarian_id>/form/', librarian_edit_form, name='librarian_edit_form'),
    path('library/<int:library_id>/form/', library_edit_form, name='library_edit_form'),
]