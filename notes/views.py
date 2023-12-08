from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from .forms import NoteForm
from .models import Note
from .serializers import NoteSerializer


class YourNoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class YourNoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

def home(request):
    notes = Note.objects.all()
    return render(request, 'notes/home.html', {'notes': notes})


def create_or_edit_note(request, note_id=None):
    if note_id is not None:
        note = get_object_or_404(Note, pk=note_id)
    else:
        note = None

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/create_or_edit_note.html', {'form': form, 'note': note})

def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('home')
    return render(request, 'notes/delete_note.html', {'note': note})