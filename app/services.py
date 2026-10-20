from app.models import Note
from app.utils import truncate


class NoteService:
    def __init__(self):
        self._notes = {}
        self._next_id = 1

    def create(self, title, content):
        note = Note(self._next_id, title, content)
        self._notes[note.id] = note
        self._next_id += 1
        return note

    def get(self, note_id):
        return self._notes.get(note_id)

    def list_all(self):
        return list(self._notes.values())

    def delete(self, note_id):
        return self._notes.pop(note_id, None) is not None

    def summaries(self):
        return [
            {"id": n.id, "title": n.title, "preview": truncate(n.content)}
            for n in self._notes.values()
        ]
