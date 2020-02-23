#!/usr/bin/env python3

# qiitaのトレンド1位の記事を記録するbot
# https://qiita.com/

import json
import datetime

from bs4 import BeautifulSoup
import psycopg2
import requests

def main():
    url = "https://qiita.com/"
    r = requests.get(url)

    values = scrape_qiita(r)
    conn = psycopg2.connect(
        database='yusuke', 
        user='yusuke', 
        password='thisistest', 
        host='127.0.0.1', 
        port=5432,
    )
    cur = conn.cursor()
    cur.execute('INSERT INTO qiita_trend VALUES (%s, %s, %s, %s)', (values[0], values[1], values[2], values[3],))
    conn.commit()
    conn.close()

def scrape_qiita(r):
    soup = BeautifulSoup(r.text, 'html.parser')
    tr_item = soup.select('[data-hyperapp-app="Trend"]')
    dic = tr_item[0]["data-hyperapp-props"]
    top_trend = json.loads(dic)['trend']['edges'][0]['node']
    return [top_trend['uuid'], datetime.date.today(), top_trend['title'], top_trend['author']['urlName']]

if __name__=='__main__':
    main()