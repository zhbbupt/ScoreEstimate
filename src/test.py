'''
Created on 2014-10-2

@author: zhanghb
'''
import datetime   
starttime = datetime.datetime.now()
import ScoreEstimate
ScoreEstimate.Estimate('data/recommendation.txt','data/result.txt')
endtime=datetime.datetime.now()
print "runtime=",endtime-starttime
