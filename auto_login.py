import subprocess
from time import sleep as sp
from os import system
username = ""
passwd = ""
url = ""


def auto_login():
    system('curl "{}/logout?" '
           '-H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0" '
           '-H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8" '
           '-H "Accept-Language: en-US,en;q=0.5" '
           '-H "Accept-Encoding: gzip, deflate" '
           '-H "Connection: keep-alive" '
           '-H "Referer: http://pignatellif.edetronik.es/status" '
           '-H "Upgrade-Insecure-Requests: 1"'.format(url))
    system('wget "{}/login?" '
           '--header "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0" '
           '--header "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8" '
           '--header "Accept-Language: en-US,en;q=0.5" --header "Accept-Encoding: gzip, deflate, br" '
           '--header "Connection: keep-alive" '
           '--header "Referer: http://pignatellif.edetronik.es/" '
           '--header "Upgrade-Insecure-Requests: 1" '
           '--header "Sec-Fetch-Dest: document" '
           '--header "Sec-Fetch-Mode: navigate" '
           '--header "Sec-Fetch-Site: cross-site" '
           '--header "Sec-Fetch-User: ?1" '
           '--no-check-certificate '
           '--post-data "username={}&password={}"'.format(url, username, passwd))
    system('del login*')
    sp(14400)
    auto_login()


def main():
    auto_login()


if __name__ == '__main__':
    main()
