#!/usr/bin/python
from Participant_class import Participant
import sys
import getopt
import os


try:
    opts, args = getopt.getopt(sys.argv[1:], 'g:i:s:d:a', ['group=', 'id=', 'sessions=', 'studydir=','addsession='])
except getopt.GetoptError:
    sys.exit(2)
    
# set inputs
for opt, arg in opts:
    if opt in ('-g', '--group'):
        group=arg
    elif opt in ('-i', '--id'):
        id = arg
    elif opt in ('-s', '--sessions'):
        ses_cnt = arg
    elif opt in ('-d', '--studydir'):
        study = arg
    elif opt in ('-a', '--addsession'):
        new_session = arg

sub1 = Participant(group,id,ses_cnt)

#   - directory exists if it doesn't exist then create it
if os.path.isdir(study) is False:
    print 'Created' ,study, 'as the parent study directory'
    os.makedirs(study)
    

print(sub1.subname)
print(study)
print(new_session)

# Checks

#   - new session should be of ses-0X format
#   - ses_cnt should be nonzero, > 0, integer
