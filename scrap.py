from bs4 import BeautifulSoup
import requests
import time

print('Put some skill that you are not familiar with')
Unfamiliar_Skills = input('>')
print(f'Filtering out {Unfamiliar_Skills}')


html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python+&txtLocation=").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

def find_jobs():

    for index,job in enumerate(jobs):
        Published_date = job.find('span', class_='sim-posted').span.text
        
        if 'few' in Published_date:
            company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            Skills = job.find('span',class_='srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']

            if Unfamiliar_Skills not in Skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(Published_date)
                    f.write(f'''Company Name: {company_name.strip()} \n''')
                    f.write(f"Required Skills: {Skills.strip()} \n")
                    f.write(f"More Info: {more_info} \n")
            
                print(f'file saved: {index}')
            

if __name__ == '__main__':
        while True:
            find_jobs()
            time_wait = 10
            print(f'Waiting {time_wait} minutes...')
            time.sleep(time_wait * 60)
            
            












# with open('Daily_Flyer.html', 'r') as html_file:
#     content = html_file.read()
    
#     soup = BeautifulSoup(content, 'lxml')
#     Offers_Card= soup.find_all('div', class_='lg:w-1/4 md:w-1/2 p-4 w-full')
#     for Offers in Offers_Card:
#         Offer_Name = Offers.h3.text
#         Offer_Time = Offers.p.text
        
#         print(Offer_Name)
#         print(Offer_Time)
    
   
    