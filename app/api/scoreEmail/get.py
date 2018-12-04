from manage import *
import sqlite3
import json
from flask_api import status

def get_Score_Email_by_dp_id(dp_id):
    '''
    This function responds to a request for /api/v1.0/scoreEmail/{dpid}
    with a list of cookies and scores connected to this data provider

    :param dp_id:    the dpid to filter the scores.
    :return:        a list of json objects which contains hash_email,score,dp_id of the respective cookie_id
    '''
    if(dp_id == None or dp_id == ""):
        content = {'please move along': 'nothing to see here'}
        return content, status.HTTP_404_NOT_FOUND

    sql = sqlite3.connect('example.db')
    cur1 = sql.cursor()
    cur1.execute('select count(1) from dataprovider_cookies where dataprovider_id =?',(dp_id,))
    p = cur1.fetchall()
    if p[0][0]==0:
        content1 = {'please move along': 'nothing to see here', 'status': status.HTTP_404_NOT_FOUND}
        return content1
    cur = sql.cursor()
    cur.execute('select * from (select DISTINCT dataprovider_id,score,hash_email from cookie_scores,dataprovider_cookies,email_cookies where cookie_scores.cookie_id = dataprovider_cookies.cookie_id and email_cookies.cookie_id = dataprovider_cookies.cookie_id) where dataprovider_id =?',(dp_id,))
    result = cur.fetchall()
    flag = 0
    hashed_emails_list = list(result[:-1])
    for hashed_email in hashed_emails_list:
        if hashed_email == None or hashed_email == "":
            continue
        else:
            flag = 1
    if(flag == 0):
        return []
    inter_list = []
    for each in result:
        json_data = dict(zip(['dp_id','score','hash_email'],each))
        inter_list.append(json_data)
    
    return inter_list
