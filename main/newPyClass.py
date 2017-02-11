'''
Created on Feb 11, 2017

@author: jinhua
'''
# -*- coding: UTF-8 -*-


class Car(object):
    '''
    a new car class
    '''
    

    def __init__(self, name,numb,mail):
        '''
        Constructor
        '''
        self.name = name
        self.num = numb
        self.mail = mail
        
    def displayCarInfo(self):
        '''
        display car's information.
        '''
        print "Name:",self.name,",Num:",self.numb,",mail:",self.mail
        