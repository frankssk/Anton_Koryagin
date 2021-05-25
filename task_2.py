import requests
import os

file_url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
file_name = 'nginx_logs.txt'
remote_addr_index = 0
ip = {}
value = 1


def download_file():
    response = requests.get(file_url, stream=True)
    with open(file_name, 'ab') as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)


def generator_pars():
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            split_line = line.split()
            remote_addr = split_line[remote_addr_index]
            yield remote_addr


def count_ip(ip_addr):
    if ip_addr not in ip:
        ip[ip_addr] = 1
    else:
        ip[ip_addr] += 1


def top_ip():
    i = 0
    ip_top = ''
    for ip_log in ip.items():
        if ip_log[value] >= i:
            i = ip_log[value]
            ip_top = ip_log
    return ip_top


def main():
    if not os.path.exists(file_name):
        download_file()
    file_pars = generator_pars()
    for log in file_pars:
        count_ip(log)
    print(top_ip())


if __name__ == '__main__':
    main()
