from dataclasses import dataclass
from datetime import datetime

# Definición de la clase Note como una dataclass
@dataclass
class Note:
    code: str
    creation_time: datetime
    title: str
    text: str
    importance: str
    tags: list

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"Code: {self.code}\nCreation date: {self.creation_time}\n{self.title}: {self.text}"

# Definición de la clase Notebook
class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, title: str, text: str, importance: str) -> str:
        code = self.generate_unique_code()
        note = Note(code, datetime.now(), title, text, importance, [])
        self.notes.append(note)
        return code

    def generate_unique_code(self) -> str:
        # Genera un código único para la nota (puede implementarse de diversas maneras)
        # Aquí, estamos usando la fecha actual y un número incremental.
        code_prefix = datetime.now().strftime("%Y%m%d%H%M%S")
        code_suffix = str(len(self.notes) + 1)
        return f"{code_prefix}-{code_suffix}"

    def list_all_notes(self):
        for note in self.notes:
            print(note)

    def add_tags_to_note(self, code: str, tags: list):
        for note in self.notes:
            if note.code == code:
                for tag in tags:
                    note.add_tag(tag)

    def important_notes(self):
        return [note for note in self.notes if note.importance in ['HIGH', 'MEDIUM']]

    def tags_note_count(self):
        tag_count = {}
        for note in self.notes:
            for tag in note.tags:
                if tag in tag_count:
                    tag_count[tag] += 1
                else:
                    tag_count[tag] = 1
        return tag_count

if __name__ == "__main__":
    notebook = Notebook()

    code1 = notebook.add_note("Important Note 1", "This is a high-priority note", "HIGH")
    code2 = notebook.add_note("Medium Note 1", "This is a medium-priority note", "MEDIUM")
    code3 = notebook.add_note("Low Note 1", "This is a low-priority note", "LOW")

    notebook.add_tags_to_note(code1, ["work", "urgent"])
    notebook.add_tags_to_note(code2, ["personal", "important"])

    print("All Notes:")
    notebook.list_all_notes()

    print("\nImportant Notes:")
    important_notes = notebook.important_notes()
    for note in important_notes:
        print(note)

    print("\nTag Counts:")
    tag_counts = notebook.tags_note_count()
    for tag, count in tag_counts.items():
        print(f"{tag}: {count} notes")
#