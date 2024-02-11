from django.view import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from crudie.models import PythonDjangoSQLData


class Base(View):
    model = PythonDjangoSQLData
    field = '__all__'


class Create(Base, CreateView):
    """Create View"""


class Read(Base, DetailView):
    """Detail View"""


class Update(Base, UpdateView):
    """Update View"""


class Delete(Base, DeleteView):
    """Delete View"""

