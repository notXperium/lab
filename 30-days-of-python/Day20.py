import webbrowser 

url_lists = [
    'http://www.python.org',
    'https://github.com',
    'https://twitter.com',
]

for url in url_lists:
    webbrowser.open_new_tab(url)