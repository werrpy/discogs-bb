import discogs_client
import requests
import argparse

class BBCode:
  def image(self, url):
    return '[center][img]' + str(url) + '[/img][/center]'

  def tracklist(self, list):
    bbcode = '[list=1]'
    for track in list:
      if not track.position and not track.title and not track.duration:
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

  def link_name(self, url, name):
    return '[url=' + str(url) + ']' + str(name) + '[/url]'

def parse_label(label):
  if label.name:
    if label.urls and len(label.urls) > 0:
      print(bb.link_name(label.urls[0], label.name), end = '')
    else:
      print(label.name, end = '')
  if label.profile:
    # split profile by paragraph
    p = label.profile.split("\n\r")
    # display first paragraph
    print(" - " + p[0])
  else:
    print("")
  # more label urls
#  if label.urls and len(label.urls) > 1:
#    for url in label.urls:
#      print(bb.link(url))

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

# BBCode formatter
bb = BBCode()

# Discogs ID = args.discogs
release = d.release(args.discogs)

# comma seperated artists
artists = ', '.join(str(artist.name) for artist in release.artists)

# artists - title
title = artists + ' - ' + release.title + ' (' + str(release.year) + ')'
print('Title: ' + title)

# comma seperated genres
if release.genres:
  tags = ', '.join(release.genres)
  print('Tags: ' + tags)

# country
if release.country:
  print('Country: ' + release.country)

# get unique labels
seen = set()
labels = [x for x in release.labels if not (x.id in seen or seen.add(x.id))]

# labels
if len(labels) > 0:
  print('Labels: ')
  for lbl in labels:
    label = d.label(lbl.id)
    parse_label(label)

# images
if release.images is not None:
  print('Images: ')
  for img in release.images:
    print(bb.image(img['uri']))

# tracklist
print('Tracklist:')
print(bb.tracklist(release.tracklist))

# Discogs url
print('Discogs: ' + bb.link('https://www.discogs.com/release/' + str(args.discogs)))
