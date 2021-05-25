import requests
import os

file_url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
file_name = 'nginx_logs.txt'
remote_addr_index = 0
request_type_index = 5
requested_resource_index = 6


def download_file():
    response = requests.get(file_url, stream=True)
    with open(file_name, 'ab') as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)


def generator_pars():
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            split_line = line.split()
            remote_addr, request_type, requested_resource = (
                split_line[remote_addr_index],
                split_line[request_type_index],
                split_line[requested_resource_index]
            )
            request_type = request_type.strip('"')
            yield remote_addr, request_type, requested_resource


def main():
    if not os.path.exists(file_name):
        download_file()
    file_pars = generator_pars()
    for log in file_pars:
        print(log)


if __name__ == '__main__':
    main()
