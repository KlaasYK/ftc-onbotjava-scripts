#!/usr/bin/env python3

"""
    Pull file from robot
"""

import argparse
import requests

address = 'http://192.168.49.1:8080/'
javafileget = 'java/file/get?f='

def main(args):

    cookieReq = requests.get(address)
    # TODO: cache this cookie
    consoleSession = cookieReq.cookies;

    print('Pulling:', address + javafileget + args.basepackage + args.file)

    fileReq = requests.get(address + javafileget + args.basepackage + args.file,
                           cookies=consoleSession)

    # TODO: check for errors

    with open(args.file, 'w') as f:
        f.write(fileReq.text)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('-p', dest='basepackage',
        default='/src/org/firstinspires/ftc/teamcode/',
        help='package directory, default = src/org/firstinspires/ftc/teamcode/')

    parser.add_argument('file', help='filename to pull')

    main(parser.parse_args())
