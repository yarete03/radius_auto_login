from os import system

url = ""

def stop():
    system('curl "{}/logout?" '
           '-H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0" '
           '-H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8" '
           '-H "Accept-Language: en-US,en;q=0.5" '
           '-H "Accept-Encoding: gzip, deflate" '
           '-H "Connection: keep-alive" '
           '-H "Referer: http://pignatellif.edetronik.es/status" '
           '-H "Upgrade-Insecure-Requests: 1"'.format(url))


def main():
    stop()


if __name__ == "__main__":
    main()
