The spotify api doesn't requesting certain information about an artist such as an artists biography, monthly listeners, top cities and more.
This workaround allows you get this information and only uses the standard library.

Grabs data from the artist about page on the spotify web player.


artist_about(artist_id, remove_bio_tags
<ul>
   <li>[str]artist_id: spotify artist id</li>
   <li>[bool]remove_bio_tags: removes the hyperlink tags from the biography [default: True]</li>
</ul>


print_keys(dict) will print the keys and nested keys in a dictionary


Example:
<ul>
   <li>external_urls<li>
   <ul>
      <li>spotify</li>
   </ul>
   <li>followers</li>
   <ul>
      <li>href</li>
      <li>total</li>
   </ul>
   <li>genres</li>
   <li>href</li>
   <li>id</li>
   <li>images</li>
   <li>name</li>
   <li>popularity</li>
   <li>type</li>
   <li>uri</li>
   <li>top_tracks</li>
   <li>insights</li>
   <ul>
      <li>artist_gid</li>
      <li>autobiography</li>
      <ul>
         <li>urls</li>
         <li>links</li>
         <ul>
            <li>twitter</li>
            <li>facebook</li>
         </ul>
      </ul>
      <li>biography</li>
      <li>header_image</li>
      <ul>
         <li>id</li>
         <li>uri</li>
         <li>width</li>
         <li>height</li>
      </ul>
      <li>images</li>
      <li>global_chart_position</li>
      <li>monthly_listeners</li>
      <li>monthly_listeners_delta</li>
      <li>follower_count</li>
      <li>following_count</li>
      <li>playlists</li>
      <ul>
         <li>entries</li>
      </ul>
      </li>cities</li>
   </ul>
</li>
