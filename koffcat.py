import sys
import socket
import getopt
import threading
import subprocess

##########
# GLOBAL #
##########
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0


def usage():
    print(open("usage.txt", "r").read())
    sys.exit(0)


if __name__ == '__main__':
    usage()
