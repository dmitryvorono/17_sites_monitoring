import requests
import whois
import os
import argparse
import sys
import datetime


def load_urls4check(path):
    if not os.path.exists(path):
        return None
    with open(path, 'r') as file_handler:
        return file_handler.read()


def is_server_respond_with_200(url, request_timeout=60):
    request = requests.get(url, timeout=request_timeout)
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


def get_domain_name(url):
    return url.split('://')[1]


def check_urls(urls):
    if urls is None:
        return None
    return [{'url': url,
             'is_respond_200': is_server_respond_with_200(url),
             'check_expiration_date': check_domain_expiration_date(get_domain_name(url))}
            for url in urls]


def check_domain_expiration_date(url):
    expiration_date = get_domain_expiration_date(url)
    return is_good_expiration_date(expiration_date)


def is_good_expiration_date(expiration_date, max_day=30):
    if expiration_date is None:
        return False
    now = datetime.datetime.now()
    time_delta = expiration_date - now
    return bool(time_delta.days >= max_day)


def print_check_urls(checks):
    if checks is None:
        return None
    for check_url in checks:
        print(check_url['url'], end=': ')
        print('[OK]' if check_url['is_respond_200'] else '[is not respond 200]', end='')
        print('[OK]' if check_url['check_expiration_date'] else '[Need to extend expiration data]')


def make_list_urls(raw_text):
    if raw_text is None:
        return None
    return raw_text.split()


def main():
    parser = create_parser()
    args = parser.parse_args()
    raw_text = load_urls4check(args.path)
    urls = make_list_urls(raw_text)
    print_check_urls(check_urls(urls))


if __name__ == '__main__':
    status = main()
    sys.exit(status)
