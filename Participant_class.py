# -*- coding: utf-8 -*-
"""
Participant Class
- Group; ms, hc etc
- ID number, 001, 002
- Sessions, can give an integer


--- Later ---
- auto lowercase
- format the ID number under sub-hc000
- adding additional session
- Age
- Gender
-------------
"""

class Participant:
    def __init__(self,group,ID,session):
        self.group=group
        self.ID=ID
        self.session=session
        
        self.subname='sub-' + group + ID
        
    
    
    """
    Functions Needed:
        - Create the study directory if it doesn't exist
        - Create the subject directory if it doesn't exist
            (will handle adding sessions later on)
    
    
    """

sub1 = Participant('ms','001',1)
print(sub1.subname)


sub2 = Participant('ms','002',1)
print(sub2.subname)