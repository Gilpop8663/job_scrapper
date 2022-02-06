import random
import requests
from bs4 import BeautifulSoup


def extract_indeed_pages(URL):
    result=requests.get(URL)
    soup = BeautifulSoup(result.text.encode('utf-8'),"html.parser")
    pagination = soup.find("ul", {"class":"pagination-list"})
    pages = pagination.find_all('span')

    spans=[]
    for page in pages[:-2]:
        spans.append(page.string)
    max_page = spans[-1]
    return int(max_page)

def extract_job(html):
    title_box=html.find("h2",{"class":"jobTitle"})
    title = title_box.find("span",title=True).string
    is_company = html.find("span",{"class":"companyName"})
    if is_company is not None:
        company =is_company.string
    else:
        company = is_company
    # print(company)
    location = html.find("div",{"class":"companyLocation"}).string
    job_id = html["data-jk"]
    return {"site":"indeed","title":title,"companyName":company,"location":location,"link":f"https://kr.indeed.com/%EC%B1%84%EC%9A%A9%EB%B3%B4%EA%B8%B0?jk={job_id}","img":"https://user-images.githubusercontent.com/80146176/152662969-959e0856-c5ef-48d2-ac73-5220742f04e7.png","like":random.randrange(1,10000),"view":random.randrange(1,10000)}

def extract_indeed_jobs(last_page,URL):
    jobs=[]
    for page in range(last_page):
        print(f"Indeed Page : {page}")
        result= requests.get(f"{URL}&start={page*50}")
        soup = BeautifulSoup(result.text,"html.parser")
        results = soup.find_all("a",{"class":"tapItem"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs(word):
    URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and={word}&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=84329a66291839cd"
    last_page=extract_indeed_pages(URL)
    jobs=extract_indeed_jobs(last_page,URL)
    return jobs