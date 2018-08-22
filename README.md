# discogs-bb
Discogs BBCode formatter

Requirements
```
pip3 install discogs_client
```

Usage
```
python3 discogsbb.py discogsid
```

Sample Output
```
> python3 discogsbb.py 105
Title: Pure Science, Mashupheadz - Tech House Phenomena 2
Tags: Electronic
Images:
[center][img]https://img.discogs.com/gp7QB8uyM9BWOYf1E8Ujzas1JVs=/fit-in/373x380/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-105-1125691988.jpeg.jpg[/img][/center]
[center][img]https://img.discogs.com/cXVBYJQUe5FuTO5Fj93MucBOQT8=/fit-in/292x292/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-105-1100127334.jpg.jpg[/img][/center]
[center][img]https://img.discogs.com/h6QAfCwmBCXBTyj1L9oUC4A3eXI=/fit-in/292x292/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-105-1100127340.jpg.jpg[/img][/center]
Tracklist:
[list=1][*]Rydym[/*][*]Pillock[/*][/list]
Discogs: [url=https://www.discogs.com/release/105]https://www.discogs.com/release/105[/url]
```

Generate a personal access token at https://www.discogs.com/settings/developers. Replace `user_token` and set a unique `user_agent` here: https://github.com/werrpy/discogs-bb/blob/master/discogsbb.py#L23-L29
