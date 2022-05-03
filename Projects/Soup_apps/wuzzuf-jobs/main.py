import os
from itertools import zip_longest
from pprint import pprint
import requests
import csv
from alive_progress import alive_bar
from bs4 import BeautifulSoup



def main():
    job_requirements = []
    job_titles = []
    company_names = []
    locations = []
    job_links = []
    job_dates = []
    # filtered within one month
    response = requests.get(
        url=f"https://wuzzuf.net/search/jobs/?a=hpb&filters%5Bpost_date%5D%5B0%5D=within_1_month&q=python&start=0")
    webbrowser = response.content
    soup = BeautifulSoup(webbrowser, 'lxml')
    total = (int(soup.find('strong').text) // 15)

    with alive_bar(total+1,bar='filling',title='Searching through available pages for Jobs') as bar:
        for page_number in range(total):
            response = requests.get(
                url=f"https://wuzzuf.net/search/jobs/?a=hpb&filters%5Bpost_date%5D%5B0%5D=within_1_month&q=python&start={page_number}")
            webbrowser = response.content
            soup = BeautifulSoup(webbrowser, 'lxml')
            job_title=soup.find_all('h2',{'class':'css-m604qf'})
            company_name=soup.find_all('a',{'class':"css-17s97q8"})
            location=soup.find_all('span',{'class':'css-5wys0k'})
            job_requirement=soup.find_all('div',{'class':'css-y4udm8'})
            dates=soup.find_all('div',{"class":"css-d7j1kk"})
            job_responsibilities=[]
            for i in range(len(job_title)):
                # pprint(f"Job Title :{job_title[i].text}")
                # pprint(f"Company name Title :{company_name[i].text}")
                # pprint(f"Job Requirement :{job_requirement[i].text}")
                # pprint(f"Job Location :{location[i].text}" )
                # pprint(f"Job Date : {dates[i].div.text}")
                # print()
                job_dates.append(dates[i].div.text)
                job_titles.append(job_title[i].text)
                job_links.append(job_title[i].find('a').attrs['href']) # to
                company_names.append(company_name[i].text)
                job_requirements.append(job_requirement[i].text)
                locations.append(location[i].text)

            for link in job_links:
                response=requests.get(url=link)
                soup=BeautifulSoup(response.content,'lxml')
                job_responsibility=soup.find('div',{'class':"css-1uobp1k"}).ul
                responsibility=""
                try:
                    all = job_responsibility.find_all('li')
                    for li in all :
                        responsibility+="-"+li.text+"\n"
                except AttributeError:
                    responsibility+='-Nothing'
                job_responsibilities.append(responsibility)

                # you only can notice it in the command line
            bar()
        file_list=[job_titles,company_names,job_dates,locations,job_requirements,job_links,job_responsibilities]
        jobs=zip_longest(*file_list)#*filelist means ==> [[a,b],[1,2]] zip_longest transform it==> [[a,1],[b,2]]

        with open('./wuzzuf_jobs.csv','w') as file:
            write=csv.writer(file)
            write.writerow(['Job Title','Company Name','Post Date','Location','Job Requirements','Job Page Links','Job Responsibilities'])
            write.writerows(jobs)
        bar()

        open_file()

def open_file():
    path = os.getcwd() + "/wuzzuf_jobs.csv"
    operating_system=os.uname().sysname
    if operating_system=="Linux":
        os.system(f"libreoffice  {path}")
    elif operating_system=="Window":
        os.system(f"excel")

if __name__ =="__main__":
   main()