from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np 
import pdb

def get_url(table_no, title):
    table_section = table_index.find('a', {'title':title})
    if table_section is not None:
        return table_section['href']
    
def test_url(page_name):
    with suppress(Exception):
        return requests.get(page_name).status_code == requests.codes.ok
    
def request_inspect_for_r2d(repo_url):
    repo_name = repo_url[len('https://github.com'):]
    file_types = ['Dockerfile', 'binder', 'apt.txt', 'environment.yml', 'requirements.txt', 'postBuild']
    repo_soup = BeautifulSoup(requests.get(repo_url).content, "html5lib")
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

def test_gh_checker():
    jlab_demo = request_inspect_for_r2d('https://github.com/jupyterlab/jupyterlab-demo')
    assert sum(jlab_demo.values) == 1
    assert jlab_demo['binder']
    latex_binder = request_inspect_for_r2d('https://github.com/jupyterlab/jupyterlab-demo')
