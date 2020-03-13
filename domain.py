from urllib.parse import urlparse

# get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except Exception as e:
        print('Exception occurred at get_domain_name() ==> {}'.format(e))
        return ''

# get subdomain name(name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except Exception as e:
        print('Exception occurred at get_sub_domain_name() ==> {}'.format(e))
        return ''

# print(get_domain_name('https://docs.python.org/3/library/email.message.html'))
# print(get_sub_domain_name('https://docs.python.org/3/library/email.message.html'))