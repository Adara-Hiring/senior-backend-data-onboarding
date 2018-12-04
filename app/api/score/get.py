from manage import *
import pandas as pd
import sqlite3
import json

def get_score_by_cookie_id(cookie_id):
    """
    This function responds to a request for /api/v1.0/intel/{dpid}
    with a list of cookies and scores connected to this data provider

    :param cookie_id:    the dpid to filter the scores.
    :return:        a cookie id and the relevant score
    """

    # result = cookie_scores.loc[cookie_scores['cookie_id'] == cookie_id, 1 ]
    sql = sqlite3.connect('example.db')
    cur = sql.cursor()

    #cur.execute('select score from cookie_scores where cookie_id ={0} '.format(cookie_id))
    cur.execute("select score from cookie_scores where cookie_id=?",(cookie_id,))
    result = cur.fetchone()
    #result_dict = dict([(cookie_id,result)])
    #result = tuple(result)
    #print(result)
    #print(result)
    if result is None:
        cur.execute("select avg(score) from cookie_scores")
        result = cur.fetchone()
        x = result[0] 
    else:
        x = result[0]

    end_res = {'cookie_id':cookie_id,'score':x}
    sql.commit()
    cur.close()

    #print(result)
    #return json.dumps(end_res)
    return end_res