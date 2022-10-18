import scrapy


class MovieSpider(scrapy.Spider):
    name = "movie"

    def start_requests(self):
        urls = [
            'https://movie.naver.com/movie/running/current.nhn',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        movie_sels = response.css(
            '#content > div.article > div > div.lst_wrap > ul > li:nth-child(1) > dl > dt > a').get()
        print()
        print()
        print(type(response))
        print(movie_sels)
        print()
        print()
        print()
