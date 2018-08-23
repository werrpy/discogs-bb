# discogs-bb
Discogs BBCode formatter

Requirements  
Python 2 or 3
```
pip install discogs_client
```

Usage
```
python discogsbb.py discogsid
```

Sample Output
```
> python discogsbb.py 12059367
Title: CHVRCHES - Love Is Dead (2018)
Tags: Electronic, Pop
Country: Australia
Labels:
[url=http://liberatormusic.com.au]Liberator Music[/url] - Liberator Music is the international recording division within the Mushroom Group.
Founded in 2006 by Nick Dunshea.
Goodbye Records (2)
Images:
[center][img]https://img.discogs.com/UGAqdJ1S1-1bXk6-a0fLl_VfBd8=/fit-in/600x532/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-12059367-1529417819-9960.jpeg.jpg[/img][/center]
[center][img]https://img.discogs.com/0raMOddBkyMYvNw8cLGW59eFjqc=/fit-in/600x533/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-12059367-1529417820-9665.jpeg.jpg[/img][/center]
[center][img]https://img.discogs.com/DB5hEEUKVCb44sWm2tLM_n1RWVs=/fit-in/600x510/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-12059367-1529417820-4941.jpeg.jpg[/img][/center]
[center][img]https://img.discogs.com/HraiOyoJlydZif3dN71OC3iIoqc=/fit-in/600x24/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-12059367-1529417819-7076.jpeg.jpg[/img][/center]
[center][img]https://img.discogs.com/77lF4zL0rjZd29qxXmUpPeZHzrY=/fit-in/600x531/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-12059367-1529417819-4120.jpeg.jpg[/img][/center]
[center][img]https://img.discogs.com/tEd2BQiF6C-XhStHhbObag6cs1Q=/fit-in/600x593/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-12059367-1529417819-9665.jpeg.jpg[/img][/center]
[center][img]https://img.discogs.com/ypFfiUhBuIpZuTtTamUqcVwLxDA=/fit-in/600x602/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-12059367-1529417819-8918.jpeg.jpg[/img][/center]
[center][img]https://img.discogs.com/qVUvzqkCBJIfgdqafS6r7yzZBHg=/fit-in/546x544/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-12059367-1529417818-9070.jpeg.jpg[/img][/center]
[center][img]https://img.discogs.com/E3400fizGnt-BNBjgIzW0CzhuqM=/fit-in/600x420/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-12059367-1529417819-4646.jpeg.jpg[/img][/center]
Tracklist:
[list=1][*]1 Graffiti 3:39[/*][*]2 Get Out 3:51[/*][*]3 Deliverance 4:13[/*][*]4 My Enemy 3:53[/*][*]5 Forever 3:44[/*][*]6 Never Say Die 4:24[/*][*]7 Miracle 3:08[/*][*]8 Graves 4:44[/*][*]9 Heaven/Hell 5:06[/*][*]10 God's Plan 3:32[/*][*]11 Really Gone 3:12[/*][*]12 ii 1:09[/*][*]13 Wonderland 4:36[/*][/list]
Discogs: [url=https://www.discogs.com/release/12059367]https://www.discogs.com/release/12059367[/url]
```

Generate a personal access token at https://www.discogs.com/settings/developers. Replace `user_token` and set a unique `user_agent` here: https://github.com/werrpy/discogs-bb/blob/master/discogsbb.py#L28-L34
