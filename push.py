#!/usr/bin/env python3

"""
    Push file to robot
"""

import argparse
import requests

address = 'http://192.168.49.1:8080/'
javafilesave = 'java/file/save?f='

def main(args):
    with open(args.file, 'r') as f:
        code = f.read()

        cookieReq = requests.get(address)
        # TODO: cache this cookie
        consoleSession = cookieReq.cookies;

        print('Pushing:', address + javafileget + args.basepackage + args.file)

        saveReq = requests.post(address + javafilesave + args.basepackage +
                                args.file, data={'data': code},
                                cookies=consoleSession)

        # TODO: check for errors
        print(saveReq)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('-p', dest='basepackage',
        default='/src/org/firstinspires/ftc/teamcode/',
        help='package directory, default = src/org/firstinspires/ftc/teamcode/')

    parser.add_argument('file', help='filename to push')

    main(parser.parse_args())
