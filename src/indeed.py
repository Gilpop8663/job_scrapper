import requests
from bs4 import BeautifulSoup

LIMIT = 50

URL =f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=react&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l&fromage=any&limit={LIMIT}&sort&psf=advsrch&from=advancedsearch&vjk=84329a66291839cd"


def extract_indeed_pages():
    result=requests.get(URL)
    soup = BeautifulSoup(result.text,"html.parser")
    # print(soup)
    pagination = soup.find("ul", {"class":"pagination-list"})
    pages = pagination.find_all('span')
    # next_button = pagination.find("a",{"aria-label":"다음"})
    spans=[]
    # start=0

    # while next_button:
    #     URL_LAST=f"https://www.indeed.com/jobs?q=python&limit=50&start={str(start*50)}"
    #     results_updated=requests.get(URL_LAST)
    #     soup_updated=BeautifulSoup(results_updated.text,"html.parser")
    #     next_button=soup_updated.find("a",{"aria-label":"다음"})
    #     if next_button == None:
    #         break
    #     start=int(start)+1
    for page in pages[:-2]:
        spans.append(page.string)
    # max_page = int(start)+1
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
    return {"title":title,"companyName":company,"location":location,"link":f"https://kr.indeed.com/%EC%B1%84%EC%9A%A9%EB%B3%B4%EA%B8%B0?jk={job_id}"}

def extract_indeed_jobs(last_page):
    jobs=[]
    for page in range(last_page):
        print(f"Indeed Page : {page}")
        result= requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text,"html.parser")
        results = soup.find_all("a",{"class":"tapItem"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page=extract_indeed_pages()
    jobs=extract_indeed_jobs(last_page)
    return jobs