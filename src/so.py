import random
import requests
from bs4 import BeautifulSoup



def get_last_page(URL):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36"}
    result=requests.get(URL,headers=headers)
    soup=BeautifulSoup(result.text.encode('utf-8'),"html.parser")
    pagination=soup.find("div",{"class":"s-pagination"}).find_all("a")
    last_page=pagination[-2].get_text(strip=True)
    return int(last_page)


def extract_job(html):
    title=html.find("h2",{"class":"fc-black-800"}).find("a").get_text()
    company,location = html.find("h3",{"class":"fc-black-700"}).find_all("span",recursive=False)
    company=company.get_text(strip=True)
    location=location.get_text(strip=True)
    job_id=html["data-jobid"]
    r = random.randrange(1,255)
    g = random.randrange(1,255)
    b = random.randrange(1,255)
    img_src=html.find("div",{"class":"mr12"}).find("img")
    if img_src ==None:
        img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Icon_None.svg/100px-Icon_None.svg.png"
    else:
        img_src=html.find("div",{"class":"mr12"}).find("img")["src"]
    return {"site":"so","title":title,"companyName":company,"location":location,"link":f"https://stackoverflow.com/jobs/{job_id}","img":"https://user-images.githubusercontent.com/80146176/152671175-ebb42cf1-2394-4905-840c-6e6d6e74b0db.png","like":random.randrange(1,10000),"view":random.randrange(1,10000),"companyImg":img_src,"r":r,"g":g,"b":b}

def extract_jobs(last_page,URL):
    jobs=[]
    for page in range(last_page):
        print(f"SO Page : {page}")
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text,"html.parser")
        results = soup.find_all("div",{"class":"-job"})
        for result in results:
            job=extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs(word):
    URL =f"https://stackoverflow.com/jobs?q={word}"
    last_page=get_last_page(URL)
    jobs = extract_jobs(last_page,URL)
    return jobs