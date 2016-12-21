import os
import unittest
import tempfile
# import IDB2
import IDB2

from IDB2 import error_wrapper, index, about_page, gods_model, heroes_model, creatures_model, myths_model, god_page, hero_page, creature_page, myth_page, static_files

class flaskTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, IDB2.app.config['DATABASE'] = tempfile.mkstemp()
        IDB2.app.config['TESTING'] = True
        self.app = IDB2.app.test_client()
        with IDB2.app.app_context():
            IDB2.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(IDB2.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/gods')
        assert b'No entries here so far' in rv.data

if __name__ == '__main__':
    unittest.main()
