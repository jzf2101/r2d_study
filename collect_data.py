from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np 
import pdb
import yaml
import json
from contextlib import suppress


def get_url(table_no, title):
    table_section = table_no.find('a', {'title':title})
    if table_section is not None:
        return table_section['href']
    
def test_url(page_name):
    with suppress(Exception):
        return requests.get(page_name).status_code == requests.codes.ok
    
def test_gh_checker():
    jlab_demo = request_inspect_for_r2d('https://github.com/jupyterlab/jupyterlab-demo')
    assert sum(jlab_demo.values) == 1
    assert jlab_demo['binder']
    latex_binder = request_inspect_for_r2d('https://github.com/jupyterlab/jupyterlab-demo')

gql_query = '{\
      repository(owner: "%s", name: "%s") {\
    description\
    stargazers {\
      totalCount\
    }\
    watchers {\
      totalCount\
    }\
    forks {\
      totalCount\
    }\
    languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {\
      nodes {\
        name\
      }\
    }\
    repositoryTopics(first: 10) {\
      nodes {\
        topic {\
          name\
        }\
      }\
    }\
  }\
}\
'

    
def graphql_social_data(org, repo, api_token, query=gql_query):
    url = 'https://api.github.com/graphql'
    headers = {'Authorization': 'token %s' % api_token}
    r = requests.post(url=url, data=json.dumps({'query': query.replace("\r\n", "\\n") % (org, repo)}), headers=headers)
    data = json.loads(r.text)['data']['repository']
    return data

def request_inspect_for_r2d(repo_url, repo_soup, file_types):
    repo_name = repo_url[len('https://github.com'):].rstrip('/')
    result_dict = {}
    for t in file_types:
        find_in_repo = repo_soup.find("a", {'class':'js-navigation-open', 'title':t})
        if find_in_repo is not None:
            if t == 'binder':
                check_path = '/tree/master/'
            else:
                check_path = '/blob/master/'
            result_dict[t] = find_in_repo['href'] == '{}{}{}'.format(repo_name, check_path, t)
        else: 
            result_dict[t] = False
    return result_dict

def process_gh_api_df(df):
    df.loc[:,'n_languages'] = [len(c['nodes']) for c in df['languages']]
    df['no_code'] = df['n_languages'] == 0
    for col in df.columns:
        if col in ['stargazers', 'watchers', 'forks']:
            df.loc[:,col] = [d['totalCount'] for d in df[col].values]
        elif col == 'languages':
            df['languages'] = [[x['name'] for x in c['nodes']] if len(c['nodes']) > 0 else [] for c in df['languages']]
        elif col == 'repositoryTopics':
            df.loc[:, col] = [[x['topic']['name'] for x in c['nodes']] if len(c['nodes']) > 0 else [] for c in df[col]]
    df['primary_language'] = [x[0] if len(x) > 0 else '' for x in df['languages']]
    df['Python'] = ['Python' in x for x in df['languages']]
    df['Julia'] = ['Julia' in x for x in df['languages']]
    df['R'] = ['R' in x for x in df['languages']]
    return df
    
    
        
            

