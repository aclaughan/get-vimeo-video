from urllib.request import urlopen, urlretrieve

import logging

urls = \
    [
        "https://player.vimeo.com/video/xxxxxxxxx",
        "https://player.vimeo.com/video/yyyyyyyyy",

    ]


str2match = '"profile":175,"width":1920,"mime":"video/mp4","fps":30,"url":"'
#
img2match = 'background: url('

name = "prefix"
file_number = 1

for url in urls:

    with urlopen(url) as response:
        filename = f"{name}{file_number:02}.mp4"

        page = str(response.read())

        start = page.find(str2match)
        start += len(str2match)
        ending = page.find('"', start)

        direct_url = page[start:ending]

        urlretrieve(direct_url, filename)

    file_number += 1

