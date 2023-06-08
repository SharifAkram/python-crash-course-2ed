def make_album(artist, title, tracks=0):
	"""Build a dictionary containing information about an album."""
	album_dict = {
		'artist': artist.title(),
		'title': title.title(),
	}
	if tracks:
		album_dict['tracks'] = tracks
	return album_dict

album = make_album('chris brown', 'breezy')
print(album)

album = make_album('drake', 'honestly, nevermind')
print(album)

album = make_album('aaliyah', 'one in a million')
print(album)

album = make_album('future', '56 nights', tracks=8)
print(album)

