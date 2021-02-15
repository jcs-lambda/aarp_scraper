import scrapy

class AARPSpider(scrapy.Spider):
    name = 'aarpspider'
    start_urls = [
        'https://jobs.aarp.org/index.php?action=advanced_search&page=search&keywords=data+engineer+python&country=United+States&state%5B%5D=&city=&zip=&zip_radius=5000&industry=&experience_level%5B%5D=Internship%2FCo-op&experience_level%5B%5D=Entry+Level&experience_level%5B%5D=Less+than+2+years&employer_type%5B%5D=Direct+Employer&min_salary=&max_salary=&salary_type=&start=',
    ]
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8',
    }

    def parse(self, response):
        for job_posting in response.css('div.list-jobs > div.row'):
            yield {
                'title': job_posting.css('a.job-link::text').get().strip(),
                'link': job_posting.css('a.job-link::attr(href)').get(),
                'company': job_posting.css('div.company-name::text').get().strip(),
                'location': job_posting.css('div.company-location::text').get().strip(),
                'description': job_posting.css('div.job-description > p::text').get().strip(),
                'posted': job_posting.css('time').attrib['datetime'],
            }

        for next_page in response.css('div.pagination-next-prev > a')[-1:]:
            yield response.follow(next_page, self.parse)
