import os
import sys
import unittest
# update path so we can import addon files
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
from resources.lib import khan


class KhanITTest(unittest.TestCase):

    ROOT_CHILDREN = [
        {'id': u'new-and-noteworthy', 'title': u'New and Noteworthy'},
        {'id': u'math', 'title': u'Math'},
        {'id': u'science', 'title': u'Science & Economics'},
        {'id': u'humanities', 'title': u'Humanities'},
        {'id': u'test-prep', 'title': u'Test Prep'},
        {'id': u'talks-and-interviews', 'title': u'Talks and Interviews'},
        {'id': u'coach-res', 'title': u'Coach Resources'}
    ]

    def test_load_topic_tree(self):
        tree = khan.load_topic_tree()

        self.assertEqual(tree['root'], KhanITTest.ROOT_CHILDREN)
        self.assertEqual(len(tree['root']), 7)

        # Check for a bunch of other known topics
        for topic in ['math', 'algebra', 'quadratics', 'factoring_quadratics']:
            self.assertTrue(len(tree[topic]) > 0)

        # Check one video dict
        known_video = {
            'mp4_url':
                u'http://s3.amazonaws.com/KA-youtube-converted/eF6zYNzlZKQ.mp4/eF6zYNzlZKQ.mp4',
            'thumbnail':
                u'http://s3.amazonaws.com/KA-youtube-converted/eF6zYNzlZKQ.mp4/eF6zYNzlZKQ.png',
            'youtube_id': u'eF6zYNzlZKQ',
            'description': u'Factoring Quadratic Expressions',
            'title': u'Factoring quadratic expressions'
        }
        self.assertEqual(tree['factoring_quadratics'][0], known_video)
