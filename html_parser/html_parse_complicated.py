#! /usr/bin/python3

from urllib.request import urlopen
from html.parser import HTMLParser


def isjob(url):
    try:
        a, b, c, d = url.split('/')
    except ValueError:
        return False
    # search like '/jobs/3540/' '/jobs/3539/'
    return a == d == '' and b == 'jobs' and c.isdigit()


class Scraper(HTMLParser):
    in_link = False # must have, cause self.in_link was not defined when  if tag == 'a' and isjob(url) is false

    def handle_starttag(self, tag, attrs):
        # <!--[if gt IE 8]><!--><html class="no-js" lang="en" dir="ltr">  <!--<![endif]-->
        # print(attrs)  # eg: attrs = [('class', 'no-js'), ('lang', 'en'), ('dir', 'ltr'), ...]
        # print(tag)   # eg: 'html'
        # print('----')
        attrs = dict(attrs)
        url = attrs.get('href', '')
        # if url != '':
        #     print('url =', url, '****tag =', tag)
        # <a> 标签定义超链接，用于从一个页面链接到另一个页面。
        # <a> 元素最重要的属性是 href 属性，它指定链接的目标
        # 在 XHTML 中，<br /> 插入一个简单的换行符
        if tag == 'a' and isjob(url):
            self.url = url
            self.in_link = True
            self.chunks = []

    def handle_data(self, data):
        # print(data)
        # print('====')
        # print('self.inlink=', self.in_link) #self.in_link 存在时，使用它，不存在时，使用同名类的静态变量
        # print('Scraper.inlink=', Scraper.in_link)
        # python 中属于对象的变量即使在类方法中也要用self.variable 访问，
        # 属于类的变量用class.variable,局部变量直接variable 访问
        if self.in_link:
            self.chunks.append(data)

    def handle_endtag(self, tag):
        if tag == 'a' and self.in_link:
            print('{} ({})'.format(''.join(self.chunks), self.url))
            self.in_link = False


if __name__ == '__main__':
    text = urlopen('http://python.org/jobs').read().decode()
    parser = Scraper()
    parser.feed(text) # HTMLParser.feed(text), text must be unicode
    parser.close()

# log:
# zxl@pc-zxl:~/Work/py_code/tidy$ ./html_parse_complicated.py 
# Quantitative Data Engineer (/jobs/3540/)
# Full Stack Python Developer (/jobs/3539/)
# Full stack Python and DevOps Engineer (/jobs/3535/)
# Full Stack Developer (Python)  (/jobs/3534/)
# Backend Developer (Python) (/jobs/3532/)
# Senior Python / Django Developer (Contract) (/jobs/3531/)
# Web Application Developer (/jobs/3528/)
# Python Developer (/jobs/3527/)
# Python Developer (/jobs/3526/)
# Django / Python developer (/jobs/3525/)
# Boston Area - Lead Python Programmer Wanted (/jobs/3524/)
# Senior Python Developer (/jobs/3523/)
# Fullstack Developer / Technical Co-Founder in DE / NL (/jobs/3522/)
# Developer (/jobs/3520/)
# Jr Data Scientist (/jobs/3519/)
# Senior Software Engineer (python, pandas) (/jobs/3516/)
# Senior Backend Engineer (/jobs/3514/)
# Junior Python Programmers Wanted (/jobs/3511/)
# Senior Software Engineer, Application Backend (/jobs/3509/)
# Lead Developer Python/Django (/jobs/3508/)
# Backend Software Engineer (/jobs/3505/)
# Senior Game Server Engineer (/jobs/3502/)
# Python Developer/Engineer (M/F/D) (/jobs/3500/)
# Python Back-end Developer (/jobs/3497/)
# Senior Full Stack Engineer with Python  (/jobs/3496/)
