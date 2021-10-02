from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm


def person_list(request):
    lista = Person.objects.all()
    return render(request, 'person.html', {'people': lista})


def person_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})


def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'Post':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'person': person})


