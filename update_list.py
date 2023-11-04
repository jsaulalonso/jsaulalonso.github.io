#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader

CHANNEL_PATTERN = 'http://127.0.0.1:6878/ace/getstream?id='
CHANNELS_FILTER = ['DAZN F1', 'M+ Liga', 'LaLiga TV', 'M+ Deportes', 'DAZN 1 HD', 'DAZN 2 HD', 'DAZN 3 HD', 'DAZN 4 HD']

src_file = open('src/channels.txt', 'r')

dest_list = []

for src_line in src_file.readlines():
    if CHANNEL_PATTERN in src_line and any(word in tmp_line for word in CHANNELS_FILTER):
        tmp_dict = {}
        tmp_dict['name'] = tmp_line.split('"')[3] + ' ' + src_line[-6:]
        if CHANNEL_PATTERN + 'acestream://' in src_line:
            tmp_dict['id'] = src_line.replace(CHANNEL_PATTERN + 'acestream://', '')
        else:
            tmp_dict['id'] = src_line.replace(CHANNEL_PATTERN, '')
        dest_list.append(tmp_dict)
    tmp_line = src_line

src_file.close()

j2_template = Environment(loader=FileSystemLoader(".")).get_template("list.m3u8.j2")
with open('list.m3u8', mode="w", encoding="utf-8") as dest_file:
    dest_file.write(j2_template.render(dest_list=dest_list))
    dest_file.close()
