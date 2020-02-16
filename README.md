The spotify api doesn't requesting certain information about an artist such as an artists biography, monthly listeners, top cities and more.
This workaround allows you get this information and only uses the standard library.

Grabs data from the artist about page on the spotify web player.

artist_about(artist_id, remove_bio_tags)
   [str]artist_id: spotify artist id
   [bool]remove_bio_tags: removes the hyperlink tags from the biography [default: True]

print_keys(dict) will print the keys and nested keys in a dictionary


Example:

external_urls
   spotify
followers
   href
   total
genres
href
id
images
name
popularity
type
uri
top_tracks
insights
   artist_gid
   autobiography
      urls
      links
         twitter
         facebook
   biography
   header_image
      id
      uri
      width
      height
   images
   global_chart_position
   monthly_listeners
   monthly_listeners_delta
   follower_count
   following_count
   playlists
      entries
   cities