#!/usr/bin/env python3

import pickle
from notes import Note

class GestorNotes:

    def __init__(self, file_notes='notes.pkl'):
        self.file_notes = file_notes

        try:
            with open(self.file_notes, 'rb') as f:
                self.notes = pickle.load(f)
        except FileNotFoundError:
            self.notes = []
    
    def save_notes(self):
        with open(self.file_notes, 'wb') as f:
            pickle.dump(self.notes, f)
        
    def add_note(self, content):
        self.notes.append(Note(content))
        self.save_notes()

    def show_note(self):
        return self.notes

    def search_note(self, search_text):
        return [note for note in self.notes if note.match(search_text)]
    
    def del_note(self, index):
        if index < len(self.notes):
            del self.notes[index]
            self.save_notes()
        else:
            print(f"\nThe index [{index}] that you give is incorrect")
