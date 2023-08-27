#!/usr/bin/env python3

CHANNEL_PATTERN = 'http://127.0.0.1:6878/ace/getstream?id='

try:
    src_file = open('src/channels.txt', 'r')

    dest_lines = ['#EXTM3U\r\n']

    for src_line in src_file.readlines():
        if CHANNEL_PATTERN in src_line:
            dest_lines.append(tmp_line)
            dest_lines.append(src_line.replace(CHANNEL_PATTERN, ''))
        tmp_line = src_line

    src_file.close()

    dest_file = open('list.m3u8', 'w')
    dest_file.writelines(dest_lines)
    dest_file.close()

except:
    print('ERROR')