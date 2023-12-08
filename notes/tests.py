from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class NoteAPITests(APITestCase):
    def test_api_note_creation(self):
        url = reverse('note-list')  # Assuming 'note-list' is the correct endpoint for note creation

        data = {
            'text': 'Your note text here',
            'category': 'Your category here',
            # Add other required fields if any
        }

        response = self.client.post(url, data, format='json')

        if response.status_code != status.HTTP_201_CREATED:
            print(f"Failed to create note. Response content: {response.content}")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, f"Expected status 201 but got {response.status_code}")
