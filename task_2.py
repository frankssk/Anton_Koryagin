import requests
import os
import re

FILE_URL = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
FILE_NAME = 'nginx_logs.txt'


def email_parse():
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                remote_addr = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)[0]
            except TypeError:
                # для IPv6 имеющихся в файле
                remote_addr = re.search(r'[\w\.]+', line)[0]
            request_datetime = \
                re.search(
                    r'([\w]+/[\w]+/[\w]+:[\d\:]+ [\+\d]+)',
                    line)[0]
            request_type = re.search(r'(POST|GET|PUT|OPTION|HEAD)', line)[0]
            requested_resource = re.search(r'/[/\w]+\ [/\w\.]+', line)[0]
            response_code_size = re.search(r'([\d]{1,3}) (\d+)', line)
            response_code = response_code_size[1]
            response_size = response_code_size[2]
            yield remote_addr, request_datetime, request_type, requested_resource, response_code, response_size


def download_file():
    response = requests.get(FILE_URL, stream=True)
    with open(FILE_NAME, 'ab') as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)


def main():
    if not os.path.exists(FILE_NAME):
        download_file()
    file_pars = email_parse()
    for log in file_pars:
        print(log)


if __name__ == '__main__':
    main()
