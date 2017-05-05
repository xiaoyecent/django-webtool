'''
@author: xiaoye
'''
#coding: utf-8
import exrex

'''a = list(exrex.generate('[Pp][a@]ssw[Oo]rd'))
print a'''

dic_bad = ['com', 'www', 'bbs', 'cn', '/', 'org', 'edu', 'xyz', 'top']
filter_list = ['!', '@', '#', '201']
dic_final = []

def url_split(url=''):
    if '://' in url:
        domain = url.split('://')[1] 
    else:
        domain = url
    #print domain
    if '/' in domain:
        domain = domain.split('/')[0]
    #print domain
    url_dics = domain.split('.')
    #print url_diclist
    return url_dics
    
    
def dic_create(url_dics):
    with open('D:\\django_test\\webtool\\tool\\dic_rule.ini', 'r') as f:
        for i in f.readlines():
            i = i.strip('\n')
            if i[0] != '#':
                rule = str(i)
    with open('D:\\django_test\\webtool\\tool\\comm_dic.txt', 'r') as f:
        comm_dics = f.readlines()
    dic_final = []
    for url_dic in url_dics:
        if url_dic not in dic_bad:
            for comm_dic in comm_dics:
                dics = list(exrex.generate(rule.format(url_dic=url_dic, comm_dic=comm_dic.strip('\n'))))
                for dic in dics:
                    if (len(dic) > 4) and (dic[0] not in filter_list):
                        dic_final.append(dic)
    #print dic_final
    fin = '.'.join(url_dics)
    dic_final.append(fin)
    return dic_final

#dic_create(url_split())    
            
    
            
