# -*- coding: utf-8 -*-
"""
Participant Class
- Group; ms, hc etc
- ID number, 001, 002
- Sessions, can give an integer
"""

class Participant:
    def __init__(self,group,ID,session,parent,addsession):
        self.group=group
        self.ID=ID
        self.session=session
        self.parent=parent
        self.subname='sub-' + group + ID
        
        return
    
    
    
    # Create a function that makes session folders/paths ready:
    #       - parent/ses-[session-label]/{anat,func,fmap,dwi}
    #
    #   ^^^^---- This then gets called from the run_file as:
    #            sub=Participant(group,id,session)
    #            sub.create(study)



    #def createpaths(self,parent,session,addsession):

        #return subpaths
    
   
