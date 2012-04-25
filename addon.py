#!/usr/bin/env python
'''
    plugin.video.khanacademy
    ~~~~~~~~~~~~~~~~~~~~~~~~

    An XBMC plugin to view Khan Acacademy lectures.

    :copyright: (c) 2012 by Jonathan Beluch
    :licese: GPLv3, see LICENSE.txt for more details.
'''
from xbmcswift2 import Plugin
from resources.lib.khan import KhanData, download_playlists_json


PLUGIN_NAME = 'Khan Academy'
PLUGIN_ID = 'plugin.video.khanacademy'
plugin = Plugin(PLUGIN_NAME, PLUGIN_ID, __file__)


@plugin.cache()
def get_khan_data():
    '''A cached function which returns playlist data from the API'''
    playlist_json = download_playlists_json()
    return KhanData(playlist_json)


KHAN_DATA = get_khan_data()


@plugin.route('/')
@plugin.route('/<category>/', name='show_category')
def main_menu(category='_root'):
    '''This view displays Categories or Playlists.

    This method does a lookup based on the passed category/playlist
    name to get the members. The "root" or base category is name
    "_root"
    '''
    items = [item.to_listitem(plugin)
             for item in KHAN_DATA.get_items(category)]
    return plugin.finish(items)


if __name__ == '__main__':
    plugin.run()
