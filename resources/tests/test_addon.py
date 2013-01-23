import os
import sys
import unittest
# update path so we can import addon files
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
import addon


class AddonTest(unittest.TestCase):

    def test_to_listitem(self):
        topic = {'id': u'new-and-noteworthy', 'title': u'New and Noteworthy'}
        topic_item = {
            'label': 'New and Noteworthy',
            'path': 'plugin://plugin.video.khanacademy/new-and-noteworthy/'
        }
        self.assertEqual(addon.to_listitem(topic), topic_item)

        video = {
            'mp4_url':
                'http://s3.amazonaws.com/KA-youtube-converted/eF6zYNzlZKQ.mp4/eF6zYNzlZKQ.mp4',
            'thumbnail':
                'http://s3.amazonaws.com/KA-youtube-converted/eF6zYNzlZKQ.mp4/eF6zYNzlZKQ.png',
            'youtube_id': u'eF6zYNzlZKQ',
            'description': u'Factoring Quadratic Expressions',
            'title': u'Factoring quadratic expressions'
        }
        video_item = {
            'label': 'Factoring quadratic expressions',
            'path':
                'http://s3.amazonaws.com/KA-youtube-converted/eF6zYNzlZKQ.mp4/eF6zYNzlZKQ.mp4',
            'is_playable': True,
            'thumbnail':
                'http://s3.amazonaws.com/KA-youtube-converted/eF6zYNzlZKQ.mp4/eF6zYNzlZKQ.png',
            'info': {
                'plot': u'Factoring Quadratic Expressions',
            }
        }
        self.assertEqual(addon.to_listitem(video), video_item)
