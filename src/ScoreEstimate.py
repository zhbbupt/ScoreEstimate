'''
Created on 2014-10-2

@author: Administrator
'''
from __future__ import division
import re

def Estimate(url_recom, url_result):
    recom = open(url_recom, 'r')
    result = open(url_result, 'r')
    read_recom = recom.readline()
    read_result=result.readline()
    r_read=r"\d{3,11}"
    dict_recom={}
    dict_result={}
    count_recom =0
    count_result=0
    #count_users=0
    users=[]
    while(read_recom != ''):
        recom_temp=re.findall(r_read,read_recom)
        count_recom+=1
        user_temp=recom_temp[0]
        news_temp=recom_temp[1]
        
        if not (user_temp in users):
            users.append(user_temp)
            #count_users+=1
            dict_recom[user_temp]=[]
            dict_recom[user_temp].append(news_temp)
        else:
            dict_recom[user_temp].append(news_temp)
            
        read_recom = recom.readline()
    recom.close()

    while(read_result!=''):
        result_temp=re.findall(r_read,read_result)
        user_temp=result_temp[0]
        news_temp=result_temp[1]
        dict_result[user_temp]= news_temp
        count_result+=1
        read_result=result.readline()
    result.close()

    #print dict_recom
    #print users,'\n' #,count_users
    #print dict_result,'\n',count_result
    
    hit_u=0
    
    for user in users:
        if dict_result.get(user) in dict_recom[user]:
            hit_u+=1;
    precision = hit_u/count_recom
    recall    = hit_u/count_result
    
    #print hit_u
    #print precision
    #print recall
    
    if hit_u!=0:
        F=2/((1/precision)+(1/recall))
        print " F=%0.20f\n hit_u=%d\n precision=%0.20f\n recall=%0.20f " %(F,hit_u,precision,recall)
    else:
        print "hit_u=%d" %hit_u   

#print Estimate('data/recommendation.txt','data/result.txt')
        