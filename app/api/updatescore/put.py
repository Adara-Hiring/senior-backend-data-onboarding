from manage import *
import sqlite3
import json
def update_score_by_cookie_id(score,cookie_id):
    '''
    sql = sqlite3.connect('example.db')
    cur = sql.cursor
    cur.execute('update cookie_scores set score =? where cookie_id =?',(score,cookie_id))
    result = cur.fetchall()
    print(result)
    return json.dumps(result)
    '''