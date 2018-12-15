from nose.tools import *
from ex48 import lexicon, parser


def test_Sentence():

    s1 = parser.Sentence(("noun", "cheese"), ("verb", "eats"), ("noun", "pigeon"))

    assert s1.subject == "cheese"
    assert s1.verb == "eats"
    assert s1.object == "pigeon"

def test_peek():
    word_list = []
    assert None == parser.peek(word_list)

    word_list = lexicon.scan("princess kill bear")

    assert "noun" == parser.peek(word_list)

    assert_equal(parser.peek([('verb', 'run'), ('direction', 'north')]), 
                                'verb')


def test_match():
    word_list = []
    assert None == parser.match(word_list, 'verb')

    word_list = lexicon.scan("bear eat princess")
    assert None == parser.match(word_list, 'verb')

    word_list = lexicon.scan("bear eat princess")
    assert ("noun", "bear") == parser.match(word_list, "noun")


    assert_equal(parser.match([('verb', 'run'), ('direction', 'north')], 'verb'),
                                ('verb', 'run'))


def test_skip():
    word_list = [('stop', 'of'), ('stop', 'the'), ('direction', 'north')]
    result = parser.skip(word_list, 'stop')

    assert_equal(result, None)
    assert_equal(word_list, [('direction', 'north')])

    word_list2 = [('stop', 'of'), ('stop', 'the'), ('direction', 'north')]
    result2 = parser.skip(word_list2, 'stop')

    assert_equal(result2, None)
    assert_equal(word_list2, [('direction', 'north')])


def test_parse_verb():
    word_list = [('stop', 'of'), ('stop', 'the'), ('verb', 'run')]
    assert_equal(parser.parse_verb(word_list), ('verb', 'run'))

    assert_raises(Exception, parser.parse_verb, [('stop', 'of'), 
                                                    ('stop', 'the'), 
                                                    ('direction', 'north')])


def test_parse_object():
    word_list = [('stop', 'of'), ('stop', 'the'), ('noun', 'honey')]
    assert_equal(parser.parse_object(word_list), ('noun', 'honey'))

    word_list2 = [('stop', 'of'), ('stop', 'the'), ('direction', 'north')]
    assert_equal(parser.parse_object(word_list2), ('direction', 'north'))

    assert_raises(Exception, parser.parse_object, [('stop', 'of'), 
                                                    ('stop', 'the'), 
                                                    ('verb', 'run')])


def test_parse_subject():
    word_list = [('stop', 'of'), ('stop', 'the'), ('noun', 'honey')]
    assert_equal(parser.parse_subject(word_list), ('noun', 'honey'))

    word_list2 = [('stop', 'of'), ('stop', 'the'), ('verb', 'run')]
    assert_equal(parser.parse_subject(word_list2), ('noun', 'player'))

    assert_raises(Exception, parser.parse_subject, [('stop', 'of'), 
                                                    ('stop', 'the'), 
                                                    ('direction', 'north')])


def test_parse_sentence():
    word_list = [('stop', 'I'), ('verb', 'shrunk'), 
                    ('stop', 'the'), ('noun', 'kids')]

    x = parser.parse_sentence(word_list)

    assert_equal(x.subject, 'player')
    assert_equal(x.verb, 'shrunk')
    assert_equal(x.object, 'kids')




# Got stuck for a while because the parameters in the sentence class
# are named differently to the attributes they're used to create.
# as well as differently to the varibales input
