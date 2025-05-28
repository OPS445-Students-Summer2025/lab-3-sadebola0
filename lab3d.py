#!/usr/bin/env python3
'''Lab 3 Inv 3 function free_space'''
# Author ID: [seneca_id]

import subprocess

def free_space():
    # Launch the Linux command to get available space in the root directory
    p = subprocess.Popen(
        "df -h | grep '/$' | awk '{print $4}'",
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )
    output = p.communicate()
    stdout = output[0].decode('utf-8').strip()
    return stdout

if __name__ == '__main__':
    print(free_space())
