import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

response = HtmlResponse(
    url='https://movie.naver.com/movie/running/current.nhn')
movie_sels = response.css(
    '#content > div.article > div > div.lst_wrap > ul > li:nth-child(1) > dl > dt > a').get()

print(movie_sels)
