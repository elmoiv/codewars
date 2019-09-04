def domain_name(url):
    for i in ['http://', 'https://', 'www.']:
        url = url.replace(i, '')
    return url.split('.')[0]
