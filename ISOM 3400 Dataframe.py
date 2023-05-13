from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from bs4 import BeautifulSoup
import time
import pandas as pd
import os
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
#State Code
driver.get('https://www23.statcan.gc.ca/imdb/p3VD.pl?Function=getVD&TVD=53971')
table=driver.find_element(By.TAG_NAME,'table')
df = pd.read_html(table.get_attribute('outerHTML'))
df1= df[0]['Alpha code'] 
statecode=df1.to_list()
statecode.remove('DC')
##Election Results
driver.get('https://www.politico.com/2022-election/results/')
result = driver.find_elements(By.CLASS_NAME,'styles_container__4COfe')[1]
results={}
results['Dem'] = int(result.find_element(By.CLASS_NAME,"styles_text-dem__JMe3u").text)
results['GOP'] = int(result.find_element(By.CLASS_NAME,'styles_text-gop__TtfJC').text)
results['Final Result']= result.find_element(By.CSS_SELECTOR,'#__next > div > div.styles_container__IP0HW.styles_is-desktop__eeJ39 > div.styles_content__cDWDJ.styles_is-desktop__eeJ39 > div > div:nth-child(1) > div > div:nth-child(4) > div.styles_content-container__zoW_T.styles_house__8aK01.styles_is-node-l__E8nkv > div.styles_text-container__f0mNy.styles_is-node-l__E8nkv > div > h2 > em').text
print(results)
a=0
##State
state = driver.find_element(By.CLASS_NAME,'styles_columns-container__Kq5vS').find_elements(By.CLASS_NAME,'styles_column__Twooh')
election_data = {'State':[],'State Code':[],'District':[],'Party':[],'Candidate':[],'Incumbent':[],'Votes':[],'PCT':[]}
statelist = []
statelist1 =statelist
for y in state:
    for x in y.find_elements(By.CLASS_NAME,'styles_is-desktop__25wLi'):
        statelist.append(x.text)
for x in statelist:
        namename = x
        driver.get(f"https://www.politico.com/2022-election/results/{x.replace(' ','-').lower()}/house/")
        nextpage = driver.find_elements(By.CLASS_NAME,'styles_link-heading__8MOi9')
        b = 0
        
        statename = statelist1[statelist.index(x)]
        statecode1 = statecode[statelist.index(x)]
        print(statecode1)
        try:
            expand = driver.find_element(By.CSS_SELECTOR, '#__next > div > div.styles_container__IP0HW.styles_is-desktop__eeJ39 > div.styles_content__cDWDJ.styles_is-desktop__eeJ39 > div > div:nth-child(6) > div > div > div > div > div > div.styles_container__UNlWX.styles_is-desktop__6FpnM > div.styles_right-pane__NSrij.styles_is-desktop__6FpnM > div > div.styles_table-container__vTHda > div.styles_footer-container__mcmjY.styles_is-desktop__0HSu0 > button > div')
        except:
            a=0
        else:
            WebDriverWait(driver,10000).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#__next > div > div.styles_container__IP0HW.styles_is-desktop__eeJ39 > div.styles_content__cDWDJ.styles_is-desktop__eeJ39 > div > div:nth-child(6) > div > div > div > div > div > div.styles_container__UNlWX.styles_is-desktop__6FpnM > div.styles_right-pane__NSrij.styles_is-desktop__6FpnM > div > div.styles_table-container__vTHda > div.styles_footer-container__mcmjY.styles_is-desktop__0HSu0 > button'))).click()
        try:
            data = driver.find_element(By.CLASS_NAME, 'styles_left-title__rNUfI')
        except:
            try:
                expand = driver.find_element(By.CSS_SELECTOR, '#__next > div > div.styles_container__IP0HW.styles_is-desktop__eeJ39 > div.styles_content__cDWDJ.styles_is-desktop__eeJ39 > div > div:nth-child(6) > div > div > div > div > div > div.styles_container__UNlWX.styles_is-desktop__6FpnM > div.styles_right-pane__NSrij.styles_is-desktop__6FpnM > div > div > div:nth-child(1) > table > tbody > tr.styles_container__Ql0Os.styles_is-desktop__vD7IN.styles_is-standard__kFai4.styles_is-table-small__9vxKY > td.styles_container__JFZyj > div > button')
            except:
                None
            else:
                WebDriverWait(driver,10000).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#__next > div > div.styles_container__IP0HW.styles_is-desktop__eeJ39 > div.styles_content__cDWDJ.styles_is-desktop__eeJ39 > div > div:nth-child(6) > div > div > div > div > div > div.styles_container__UNlWX.styles_is-desktop__6FpnM > div.styles_right-pane__NSrij.styles_is-desktop__6FpnM > div > div > div:nth-child(1) > table > tbody > tr.styles_container__Ql0Os.styles_is-desktop__vD7IN.styles_is-standard__kFai4.styles_is-table-small__9vxKY > td.styles_container__JFZyj > div > button'))).click()
            try:
                expand = driver.find_element(By.CSS_SELECTOR, '#__next > div > div.styles_container__IP0HW.styles_is-desktop__eeJ39 > div.styles_content__cDWDJ.styles_is-desktop__eeJ39 > div > div:nth-child(6) > div > div > div > div > div > div.styles_container__UNlWX.styles_is-desktop__6FpnM > div.styles_right-pane__NSrij.styles_is-desktop__6FpnM > div > div.styles_table-container__vTHda > div:nth-child(3) > table > tbody > tr.styles_container__Ql0Os.styles_is-desktop__vD7IN.styles_is-table__LgCr7.styles_is-table-standard___ZbiH > td.styles_container__JFZyj.styles_is-table__lpu3C > div > button')
            except:
                None
            else:
                WebDriverWait(driver,10000).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#__next > div > div.styles_container__IP0HW.styles_is-desktop__eeJ39 > div.styles_content__cDWDJ.styles_is-desktop__eeJ39 > div > div:nth-child(6) > div > div > div > div > div > div.styles_container__UNlWX.styles_is-desktop__6FpnM > div.styles_right-pane__NSrij.styles_is-desktop__6FpnM > div > div.styles_table-container__vTHda > div:nth-child(3) > table > tbody > tr.styles_container__Ql0Os.styles_is-desktop__vD7IN.styles_is-table__LgCr7.styles_is-table-standard___ZbiH > td.styles_container__JFZyj.styles_is-table__lpu3C > div > button'))).click()    
            for y in driver.find_elements(By.CLASS_NAME, 'styles_container__sXqdi'):
                        
                        name1 = y.find_element(By.CLASS_NAME,'styles_container__RbpeM').text.split()
                        name2 = list(y.find_element(By.CLASS_NAME,'styles_container__RbpeM').text)
                
                        if '(R)' in name1:
                            election_data['Party'].append('Republican')
                        elif '(D)' in name1 :
                            election_data['Party'].append('Democratic')
                        elif   '(Libertarian' in name1:
                            election_data['Party'].append('Libertarian Party')
                        elif '(Green' in name1:
                            election_data['Party'].append('Green Party')
                        elif '(Ind.)' in name1:
                            election_data['Party'].append('Ind.')
                        else:
                            election_data['Party'].append('N/A')
                        if '*' in name2:
                            election_data['Incumbent'].append('Incumbent')
                        else:
                            election_data['Incumbent'].append('/')
                        if '(R)' in name1 or '(D)' in name1 or '(Ind.)'in name1 :
                            del name1[-1]   
                            name1[-1] =name1[-1].replace('*','')       
                            election_data['Candidate'].append(''.join(name1))
                        elif '(Libertarian'  in name1 or  '(Green' in name1:
                            del name1[-2:]
                            name1[-1] =name1[-1].replace('*','')       
                            election_data['Candidate'].append(''.join(name1))
                        else:
                            name1[-1] =name1[-1].replace('*','')       
                            election_data['Candidate'].append(''.join(name1))
                       
                        election_data['District'].append('1st')
                        election_data['State'].append(statename)
                        election_data['State Code'].append(statecode1)
                        try:
                            a = y.find_element(By.CLASS_NAME,'styles_container__MY5SI').text
                            if a != '':
                                election_data['Votes'].append(y.find_element(By.CLASS_NAME,'styles_container__MY5SI').text)
                            else:
                                election_data['Votes'].append('N/A')
                            election_data['PCT'].append(y.find_element(By.CLASS_NAME,'styles_container__vzwvV').text)
                        except:
                            election_data['Votes'].append('N/A')
                            election_data['PCT'].append('N/A')
        else:
            data = driver.find_elements(By.CLASS_NAME, 'styles_left-title__rNUfI')
            for x in data:
                print(b)
                if len(data)>1:
                    
                    if b >=1:
                        
                        try:
                            expand = driver.find_element(By.CSS_SELECTOR, f"#__next > div > div.styles_container__IP0HW.styles_is-desktop__eeJ39 > div.styles_content__cDWDJ.styles_is-desktop__eeJ39 > div > div:nth-child(6) > div > div > div > div > div > div.styles_container__UNlWX.styles_is-desktop__6FpnM > div.styles_right-pane__NSrij.styles_is-desktop__6FpnM > div > div.styles_table-container__vTHda > div:nth-child({b}) > table > tbody > tr.styles_container__Ql0Os.styles_is-desktop__vD7IN.styles_is-table__LgCr7.styles_is-table-standard___ZbiH > td.styles_container__JFZyj.styles_is-table__lpu3C > div > button")
                        except:
                            None
                        else:
                            WebDriverWait(driver,10000).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"#__next > div > div.styles_container__IP0HW.styles_is-desktop__eeJ39 > div.styles_content__cDWDJ.styles_is-desktop__eeJ39 > div > div:nth-child(6) > div > div > div > div > div > div.styles_container__UNlWX.styles_is-desktop__6FpnM > div.styles_right-pane__NSrij.styles_is-desktop__6FpnM > div > div.styles_table-container__vTHda > div:nth-child({b}) > table > tbody > tr.styles_container__Ql0Os.styles_is-desktop__vD7IN.styles_is-table__LgCr7.styles_is-table-standard___ZbiH > td.styles_container__JFZyj.styles_is-table__lpu3C > div > button"))).click()
                            print(1)    
                        District = x.find_element(By.CLASS_NAME,'styles_is-desktop__4Cq7X').text
                        for y in x.find_elements(By.CLASS_NAME, 'styles_container__sXqdi'):
                            
                            name1 = y.find_element(By.CLASS_NAME,'styles_container__RbpeM').text.split()
                            name2 = list(y.find_element(By.CLASS_NAME,'styles_container__RbpeM').text)
                            if '(R)' in name1:
                                election_data['Party'].append('Republican')
                            elif '(D)' in name1 :
                                election_data['Party'].append('Democratic')
                            elif   '(Libertarian' in name1 :
                                election_data['Party'].append('Libertarian Party')
                            elif '(Green' in name1:
                                election_data['Party'].append('Green Party')
                            elif '(Ind.)' in name1:
                                election_data['Party'].append('Ind.')
                            else:
                                election_data['Party'].append('N/A')
                            if '*' in name2:
                                election_data['Incumbent'].append('Incumbent')
                            else:
                                election_data['Incumbent'].append('/')

                            if '(R)' in name1 or '(D)' in name1 or '(Ind.)'in name1 :
                                del name1[-1]   
                                name1[-1] =name1[-1].replace('*','')       
                                election_data['Candidate'].append(''.join(name1))
                            elif '(Libertarian'  in name1 or  '(Green' in name1:
                                del name1[-2:]
                                name1[-1] =name1[-1].replace('*','')       
                                election_data['Candidate'].append(''.join(name1))
                            else:
                                name1[-1] =name1[-1].replace('*','')       
                                election_data['Candidate'].append(''.join(name1))
                           
                            election_data['District'].append(District)
                            election_data['State'].append(statename)
                            election_data['State Code'].append(statecode1)
                            try:
                                a = y.find_element(By.CLASS_NAME,'styles_container__MY5SI').text
                                if a != '':
                                    election_data['Votes'].append(y.find_element(By.CLASS_NAME,'styles_container__MY5SI').text)
                                else:
                                    election_data['Votes'].append('N/A')
                                election_data['PCT'].append(y.find_element(By.CLASS_NAME,'styles_container__vzwvV').text)
                            except:
                                election_data['Votes'].append('N/A')
                                election_data['PCT'].append('N/A')
                        b+=1
                    else:
                        b+=1
            
        driver.get('https://www.politico.com/2022-election/results/')
os.chdir('C://Users//Miku//Downloads')
print(pd.DataFrame.from_dict(election_data).to_csv('hi.csv'))

            



#__next > div > div.styles_container__IP0HW.styles_is-desktop__eeJ39 > div.styles_content__cDWDJ.styles_is-desktop__eeJ39 > div > div:nth-child(6) > div > div > div > div > div > div.styles_container__UNlWX.styles_is-desktop__6FpnM > div.styles_right-pane__NSrij.styles_is-desktop__6FpnM > div > div.styles_table-container__vTHda > div.styles_footer-container__mcmjY.styles_is-desktop__0HSu0 > button
#__next > div > div.styles_container__IP0HW.styles_is-desktop__eeJ39 > div.styles_content__cDWDJ.styles_is-desktop__eeJ39 > div > div:nth-child(6) > div > div > div > div > div > div.styles_container__UNlWX.styles_is-desktop__6FpnM > div.styles_right-pane__NSrij.styles_is-desktop__6FpnM > div > div.styles_table-container__vTHda > div:nth-child(3) > table > tbody > tr.styles_container__Ql0Os.styles_is-desktop__vD7IN.styles_is-table__LgCr7.styles_is-table-standard___ZbiH > td.styles_container__JFZyj.styles_is-table__lpu3C > div > button
#__next > div > div.styles_container__IP0HW.styles_is-desktop__eeJ39 > div.styles_content__cDWDJ.styles_is-desktop__eeJ39 > div > div:nth-child(6) > div > div > div > div > div > div.styles_container__UNlWX.styles_is-desktop__6FpnM > div.styles_right-pane__NSrij.styles_is-desktop__6FpnM > div > div.styles_table-container__vTHda > div:nth-child(2) > table > tbody > tr.styles_container__Ql0Os.styles_is-desktop__vD7IN.styles_is-table__LgCr7.styles_is-table-standard___ZbiH > td.styles_container__JFZyj.styles_is-table__lpu3C > div > button
#__next > div > div.styles_container__IP0HW.styles_is-desktop__eeJ39 > div.styles_content__cDWDJ.styles_is-desktop__eeJ39 > div > div:nth-child(6) > div > div > div > div > div > div.styles_container__UNlWX.styles_is-desktop__6FpnM > div.styles_right-pane__NSrij.styles_is-desktop__6FpnM > div > div > div:nth-child(1) > table > tbody > tr.styles_container__Ql0Os.styles_is-desktop__vD7IN.styles_is-standard__kFai4.styles_is-table-small__9vxKY > td.styles_container__JFZyj > div > button
#__next > div > div.styles_container__IP0HW.styles_is-desktop__eeJ39 > div.styles_content__cDWDJ.styles_is-desktop__eeJ39 > div > div:nth-child(6) > div > div > div > div > div > div.styles_container__UNlWX.styles_is-desktop__6FpnM > div.styles_right-pane__NSrij.styles_is-desktop__6FpnM > div > div.styles_table-container__vTHda > div.styles_footer-container__mcmjY.styles_is-desktop__0HSu0 > button
#__next > div > div.styles_container__IP0HW.styles_is-desktop__eeJ39 > div.styles_content__cDWDJ.styles_is-desktop__eeJ39 > div > div:nth-child(6) > div > div > div > div > div > div.styles_container__UNlWX.styles_is-desktop__6FpnM > div.styles_right-pane__NSrij.styles_is-desktop__6FpnM > div > div > div:nth-child(1) > table > tbody > tr.styles_container__Ql0Os.styles_is-desktop__vD7IN.styles_is-standard__kFai4.styles_is-table-small__9vxKY > td.styles_container__JFZyj > div > button