#! /usr/bin/python3

from urllib.request import urlopen
from html.parser import HTMLParser


def isjob(url):
    try:
        a, b, c, d = url.split('/')
    except ValueError:
        return False
    return a == d == '' and b == 'jobs' and c.isdigit()


class Scraper(HTMLParser):
    in_link = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        url = attrs.get('href', '')
        if tag == 'a' and isjob(url):
            self.url = url
            self.in_link = True
            self.chunks = []

    def handle_data(self, data):
        if self.in_link:
            self.chunks.append(data)

    def handle_endtag(self, tag):
        if tag == 'a' and self.in_link:
            print('{} ({})'.format(''.join(self.chunks), self.url))
            self.in_link = False


if __name__ == '__main__':
    text = urlopen('http://python.org/jobs').read().decode()
    parser = Scraper()
    parser.feed(text)
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
