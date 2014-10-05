# -*- coding: utf-8 -*-

'''
Created on 2 Oct 2014

@author: zhanghb
'''
import datetime   
starttime = datetime.datetime.now()
import ScoreEstimate
ScoreEstimate.Estimate('../data/recommendation.txt', '../data/result.txt')
endtime = datetime.datetime.now()
print " runtime=", endtime - starttime
