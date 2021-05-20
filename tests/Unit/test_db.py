from unittest import TestCase
from website.models import db
from website.models import  Note , Work

class Test_database(TestCase):
    def test_note_table(self):
        note = Note(id = 1, data = "Odwa", date = 2020/5/21, user_id = 1)
        self.assertEqual(note.id, 1)
        self.assertEqual(note.data, "Odwa")
        self.assertEqual(note.date, 2020/5/21)
        self.assertEqual(note.user_id, 1)

    def test_work_table(self):
        work = Work(id = 2, title = 'TheDyans', description = 'No_work_no_pay', date = 2020/5/20 )

        self.assertEqual(work.id, 2)
        self.assertEqual(work.title, 'TheDyans')
        self.assertEqual(work.description, 'No_work_no_pay')
        self.assertEqual(work.date, 2020/5/20)

