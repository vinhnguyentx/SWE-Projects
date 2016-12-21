"""
    Tests for IDB3.py and app/models.py
"""

from IDB3 import app, generateQuery, boldSearchTerms
from unittest import main, TestCase
from app.models import db, God, Hero, Location, Myth

GOD_COLS = ['name', 'power', 'romanname', 'power', 'symbol', 'father', 'mother']
HERO_COLS = ['name', 'herotype', 'father', 'mother', 'power', 'home']
LOCATION_COLS = ['name', 'altname', 'myth', 'locationtype', 'gods']
MYTH_COLS = ['name', 'description', 'gods', 'nongods', 'place', 'theme']
MODELS_TO_COLS = {
    God: GOD_COLS,
    Hero: HERO_COLS,
    Location: LOCATION_COLS,
    Myth: MYTH_COLS
}


class TestIDB(TestCase):



    def setUp(self):
        # Create Flask test client
        self.app = app.test_client()
        self.maxDiff = None
        # self.a = [index, about_page, gods_model, heroes_model, creatures_model, myths_model, god_page, hero_page, location_page, myth_page, static_files, ]

    #------
    # index
    #------

    def test_index_1(self):
        self.assertEqual(self.app.get('/').status, '200 OK')

    def test_index_2(self):
        self.assertEqual(self.app.get('/gods/').status, '200 OK')

    def test_index_3(self):
        self.assertEqual(self.app.get('/god/').status, '404 NOT FOUND')

    def test_index_4(self):
        self.assertEqual(self.app.get('/gods/zeus/').status, '200 OK')

    def test_index_5(self):
        self.assertEqual(self.app.get('/gods/zeu').status, '301 MOVED PERMANENTLY')

    def test_index_6(self):
        self.assertEqual(self.app.get('/heroes/').status, '200 OK')

    def test_index_7(self):
        self.assertEqual(self.app.get('/hero/').status, '404 NOT FOUND')

    def test_index_8(self):
        self.assertEqual(self.app.get('/heroes/apollo/').status, '200 OK')

    def test_index_9(self):
        self.assertEqual(self.app.get('/heroes/apoll').status, '301 MOVED PERMANENTLY')

    def test_index_10(self):
        self.assertEqual(self.app.get('/heroes/somehero/').status, '200 OK')

    def test_index_11(self):
        self.assertEqual(self.app.get('/about/').status, '200 OK')

    def test_index_12(self):
        self.assertEqual(self.app.get('/about').status, '301 MOVED PERMANENTLY')

    def test_index_13(self):
        self.assertEqual(self.app.get('/bout/').status, '404 NOT FOUND')

    def test_index_14(self):
        self.assertEqual(self.app.get('/about/something/').status, '404 NOT FOUND')

    def test_index_15(self):
        self.assertEqual(self.app.get('/locations/').status, '200 OK')

    def test_index_16(self):
        self.assertEqual(self.app.get('/location/').status, '404 NOT FOUND')

    def test_index_17(self):
        self.assertEqual(self.app.get('/locations/troy/').status, '200 OK')

    def test_index_18(self):
        self.assertEqual(self.app.get('/locations/someplace/').status, '200 OK')

    def test_index_19(self):
        self.assertEqual(self.app.get('/locations/troys').status, '301 MOVED PERMANENTLY')

    def test_index_20(self):
        self.assertEqual(self.app.get('/gods/somegod/').status, '200 OK')

    def test_index_21(self):
        self.assertEqual(self.app.get('/myths/').status, '200 OK')

    def test_index_22(self):
        self.assertEqual(self.app.get('/myth/').status, '404 NOT FOUND')

    def test_index_23(self):
        self.assertEqual(self.app.get('/myths/The Myth of Europe/').status, '200 OK')

    def test_index_24(self):
        self.assertEqual(self.app.get('/myths/somemyths/').status, '200 OK')

    def test_index_25(self):
        self.assertEqual(self.app.get('/myths/troys').status, '301 MOVED PERMANENTLY')

    def test_index_26(self):
        self.assertEqual(self.app.get('/search/zeus').status, '404 NOT FOUND')

    def test_index_27(self):
        self.assertEqual(self.app.get('/search/gods').status, '404 NOT FOUND')

    def test_index_28(self):
        self.assertEqual(self.app.get('/search/heroes').status, '404 NOT FOUND')

    def test_index_29(self):
        self.assertEqual(self.app.get('/search/locations').status, '404 NOT FOUND')

    def test_index_30(self):
        self.assertEqual(self.app.get('/search/myths').status, '404 NOT FOUND')


    #-------
    # models
    #-------

    def test_models_work(self):
        for model in MODELS_TO_COLS:
            with self.subTest(model=model):
                self.assertNotEqual(len(model.query.all()), 0)

    def test_models_correct_cols(self):
        for model in MODELS_TO_COLS:
            with self.subTest(model=model):
                for col in MODELS_TO_COLS[model]:
                    with self.subTest(col=col):
                        self.assertTrue(hasattr(model, col))

    def test_models_repr(self):
        for model in MODELS_TO_COLS:
            with self.subTest(model=model):
                result = model.query.first()
                name = result.name
                expected = '<' + type(result).__name__ + " '" + name + "'>"
                self.assertEqual(expected, str(result))

    #-------
    # search
    #-------

    def test_generate_query_terms(self):
        result = generateQuery("hera zeus", 'gods', [])
        self.assertTrue('hera' in result[0])
        self.assertTrue('hera' in result[1])
        self.assertTrue('zeus' in result[0])
        self.assertTrue('zeus' in result[1])

    def test_generate_query_table(self):
        result = generateQuery("hera zeus", 'gods', [])
        self.assertTrue('god' in result[0])
        self.assertTrue('god' in result[1])

    def test_generate_query_columns(self):
        cols = ['name', 'romanname', 'power', 'symbol', 'father', 'mother']
        result = generateQuery("hera zeus", 'gods', cols)
        for col in cols:
            with self.subTest(col=col):
                self.assertTrue(col in result[0])
                self.assertTrue(col in result[1])

    def test_generate_query_correct_join(self):
        result = generateQuery("hera zeus", 'gods', [])
        self.assertTrue('intersect' in result[0].lower())
        self.assertTrue('union' in result[1].lower())


    #-----------------
    # bold search term
    #-----------------

    def test_bold_search_term_1(self):
        result = boldSearchTerms('hi', 'hi')
        self.assertEqual('<b>hi</b>', result)

    def test_bold_search_term_2(self):
        result = boldSearchTerms('idb', 'swe idb is fun')
        self.assertEqual('swe <b>idb</b> is fun', result)

    def test_bold_search_term_3(self):
        result = boldSearchTerms('bleh', 'swe idb is fun')
        self.assertEqual('swe idb is fun', result)


#------
# main
#------
if __name__ == "__main__" :
    main()

