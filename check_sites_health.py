import requests
import whois
import os
import argparse
import sys
import datetime
import pprint


def load_urls4check(path):
    if not os.path.exists(path):
        return None
    with open(path, 'r') as file_handler:
        return file_handler.read()


def is_server_respond_with_200(url, request_timeout=60):
    request = requests.get('http://' + url, timeout=request_timeout)
    return request.status_code == requests.codes.ok


def get_domain_expiration_date(domain_name):
    whois_info = whois.whois(domain_name)
    if type(whois_info.expiration_date) is list:
        whois_info.expiration_date = whois_info.expiration_date[0]
    return whois_info.expiration_date


def create_parser():
    parser = argparse.ArgumentParser(description='This script check sites')
    parser.add_argument('path', type=str, help='Path to file incude urls')
    return parser


def check_urls(urls):
    return [{'url': url,
             'is_respond_200': is_server_respond_with_200(url),
             'check_expiration_date': check_domain_expiration_date(url)}
            for url in urls]


def check_domain_expiration_date(url):
    expiration_date = get_domain_expiration_date(url)
    if expiration_date is None:
        return False
    return is_good_expiration_date(expiration_date)


def is_good_expiration_date(expiration_date, max_day=30):
    now = datetime.datetime.now()
    time_delta = expiration_date - now
    return bool(time_delta.days >= max_day)


def print_check_urls(checks):
    for check_url in checks:
        print(check_url['url'], end=': ')
        print('[OK]' if check_url['is_respond_200'] else '[is not respond 200]', end='')
        print('[OK]' if check_url['check_expiration_date'] else '[Need to extend expiration data]')


def main():
    parser = create_parser()
    args = parser.parse_args()
    urls = load_urls4check(args.path)
    if urls is None:
        return 0
    print_check_urls(check_urls(urls.split()))


if __name__ == '__main__':
    status = main()
    sys.exit(status)
