from django.urls import path
from .views import YourNoteListCreateAPIView, YourNoteDetailAPIView, home, create_or_edit_note, delete_note

urlpatterns = [
    path('api/notes/', YourNoteListCreateAPIView.as_view(), name='note-list'),
    path('api/notes/<int:pk>/', YourNoteDetailAPIView.as_view(), name='note-detail'),
    path('', home, name='home'),
    path('create_or_edit_note/', create_or_edit_note, name='create_or_edit_note'),
    path('delete_note/<int:note_id>/', delete_note, name='delete_note'),
]
