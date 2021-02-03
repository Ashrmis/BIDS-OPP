#!/usr/bin/python

from Participant_class import Participant
import sys

import getopt


try:
    opts, args = getopt.getopt(sys.argv[1:], 'g:i:s', ['group=', 'id=', 'sessions='])
except getopt.GetoptError:
    sys.exit(2)




for opt, arg in opts:
    if opt in ('-g', '--group'):
        group=arg
    elif opt in ('-i', '--id'):
        id = arg
    elif opt in ('-s', '--sessions'):
        ses_cnt = arg


sub1 = Participant(group,id,ses_cnt)

print(sub1.subname)
