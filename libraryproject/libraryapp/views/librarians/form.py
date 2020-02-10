import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Librarian
from libraryapp.models import Library
from libraryapp.models import model_factory
from ..connection import Connection


def get_librarians():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Librarian)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            l.id,
            l.location_id,
            l.user_id
        from libraryapp_librarian l
        """)

        return db_cursor.fetchall()

@login_required
def librarian_form(request):
    if request.method == 'GET':
        librarians = get_librarians()
        template = 'librarians/form.html'
        context = {
            'all_librarians': librarians
        }

        return render(request, template, context)