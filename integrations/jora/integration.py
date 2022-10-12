from requests import get
from bs4 import BeautifulSoup

class Jora:
    url = 'jora.com'
    region = 'us'
    search = ''
    location = ''

    predefined_regions = ['us', 'ca', 'br', 'uk', 'pt']

    def get_results(self):
        parsed_result = list()

        if (self.region == '*' or isinstance(self.region, list)):
            region_list = self.predefined_regions if self.region == '*' else self.region

            for region in region_list:
                self.region = region

                data = self.request()

                parsed_result.extend(self.parse(data))
        else:
            data = self.request()
            parsed_result = self.parse(data)

        return parsed_result


    def request(self):
        url = f'https://{self.region}.{self.url}/j'
        params = {
            "q": self.search,
            "l": self.location
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v1044840544831109447 t5534040873462942519 ath5ee645e0 altpriv cvcv=2 smf=0"
        }

        response = get(url, params=params, headers=headers, timeout = 30)
        return response.text
    
    def parse(self, data):
        parsed_html = BeautifulSoup(data, 'html.parser')
        job_cards = parsed_html.select('[class~=job-card]')

        jobs = list()

        for card in job_cards:
            title_tag = card.select_one('.job-link')
            company = card.select_one('.job-company')
            location = card.select_one('.job-location')
            summary = card.select_one('.job-abstract')

            jobs.append({
                "title": title_tag.string,
                "link": f'https://{self.region}.{self.url}{title_tag["href"]}',
                "company": company.string,
                "location": location.string,
                "summary": summary.string
            })

        return jobs