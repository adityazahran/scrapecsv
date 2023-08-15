from bs4 import BeautifulSoup
import requests
import time
import csv


# Filter unfamiliar skill
print("Put some skill that you are not familiar with")
unfamiliar_skill = input('>')
print(f"Filtering out {unfamiliar_skill}")

# request website
html_text = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')

# scraping


def find_jobs():
    # CSV Setup
    csv_file = open('jobs.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(csv_file)
    header = ['Company Name', 'Required Skills', 'More Info']
    writer.writerow(header)
    # Scrape
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find(
                'h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find(
                'span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
        # print(published_date)
            if unfamiliar_skill not in skills:
                data = [company_name.strip(), skills.strip(), more_info]
                writer.writerow(data)
                print(f'File saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
    csv_file.close()
