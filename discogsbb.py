import discogs_client
import requests
import argparse

class BBCode:
  def image(self, url):
    return '[center][img]' + str(url) + '[/img][/center]'

  def tracklist(self, list):
    bbcode = '[list=1]'
    for track in list:
      if not track.position or not track.title or not track.duration:
        break
      bbcode += '[*]'
      if track.position:
        bbcode += track.position
      if track.title:
        bbcode += ' ' + track.title
      if track.duration:
        bbcode += ' ' + track.duration
      bbcode += '[/*]'
    bbcode += '[/list]'
    return bbcode

  def link(self, url):
    return '[url=' + str(url) + ']' + str(url) + '[/url]'

# Discogs personal access token
# https://www.discogs.com/settings/developers
user_token = 'NFHgaaPhqdTByXxfjSEWpIBtXAGgnRcNnhnoMzqh'

# A user-agent is required with Discogs API requests. Be sure to make your user-agent
# unique, or you may get a bad response.
user_agent = 'DiscogsBBCode/1.0'

# Authenticate
d = discogs_client.Client(user_agent, user_token=user_token)

# Parse arguments
parser = argparse.ArgumentParser(description='Discogs API')
parser.add_argument('discogs', type=int, help='Discogs ID')
args = parser.parse_args()

# Discogs ID = args.discogs
release = d.release(args.discogs)

# comma seperated artists
artists = ', '.join(str(artist.name) for artist in release.artists)

# artists - title
title = artists + ' - ' + release.title
print('Title: ' + title)

# comma seperated genres
tags = ','.join(release.genres)
print('Tags: ' + tags)

# BBCode formatter
bb = BBCode()

# images
print('Images: ')
if release.images is not None:
  for img in release.images:
    print(bb.image(img['uri']))

# tracklist
print('Tracklist:')
print(bb.tracklist(release.tracklist))

# Discogs url
print('Discogs: ' + bb.link('https://www.discogs.com/release/' + str(args.discogs)))
