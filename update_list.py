#!/usr/bin/env python3

CHANNEL_PATTERN = 'http://127.0.0.1:6878/ace/getstream?id='
CHANNELS_FILTER = ['DAZN', 'Liga', 'LigaTv', 'LaLiga', 'F1', 'M+Deportes']

try:
    src_file = open('src/channels.txt', 'r')

    dest_lines = ['#EXTM3U\r\n']

    for src_line in src_file.readlines():
        if CHANNEL_PATTERN in src_line and any(word in tmp_line for word in CHANNELS_FILTER):
            dest_lines.append(tmp_line)
            if CHANNEL_PATTERN + 'acestream://' in src_line:
                dest_lines.append(src_line.replace(CHANNEL_PATTERN + 'acestream://', ''))
            else:
                dest_lines.append(src_line.replace(CHANNEL_PATTERN, ''))
        tmp_line = src_line

    src_file.close()

    dest_file = open('list.m3u8', 'w')
    dest_file.writelines(dest_lines)
    dest_file.close()

except:
    print('ERROR')