#!/usr/bin/python
from Participant_class import Participant
import sys
import getopt
import os
import argparse

#try:
#opts, args = getopt.getopt(sys.argv[1:], 'g:i:s:d:a',['group=','id=','sessions=','studydir=','addsession='])
#except getopt.GetoptError:
    #sys.exit(2)
    
parser = argparse.ArgumentParser(description='Create empty BIDS file structure')
parser.add_argument('-i','--id',metavar='',required=True,type=str, help='ID of participant i.e 001')
parser.add_argument('-g','--group',metavar='',type=str,required=True, help='Group of participant i.e ms, hc, tbi')
parser.add_argument('-s','--sessions',metavar='',type=int,required=True, help='Number of sessions i.e 2')
parser.add_argument('-d','--study',metavar='',type=str,required=True, help='Path of study directory i.e /usr/USERS/test1')
#parser.add_argument('-a','--addsession',metavar='',type=str,required=True, help='Session to add i.e ses-02')
parser.add_argument('-a','--addsession', nargs='?',type=str, default='', help='Session to add i.e. ses-02')

args=parser.parse_args()


sys.exit()

args.id
args.group
args.sessions
args.study
args.addsession

sub1 = Participant(group,id,ses_cnt)

#   - directory exists if it doesn't exist then create it
if os.path.isdir(study) is False:
    print 'Created' ,study, 'as the parent study directory'
    os.makedirs(study)
    

print(sub1.subname)
print(study)

# Checks

#   - new session should be of ses-0X format
#   - ses_cnt should be nonzero, > 0, integer

