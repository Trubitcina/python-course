import requests
import re


start = 'https://en.wikipedia.org/wiki/Coregonus_lavaretus'
stop = 'https://en.wikipedia.org/wiki/Freshwater_whitefish'


def find_urls(url):
    r = requests.get(url)
    raw_wikilinks = re.findall('/wiki/[\w]+', r.text)
    wikilinks = []
    for i in range(len(raw_wikilinks)):
        wikilinks.append("https://en.wikipedia.org" + raw_wikilinks[i])
    return wikilinks


def find_out(start, stop):
    wiki = find_urls(start)
    if stop in wiki:
        return start, stop
    else:
        for w1 in wiki:
            wiki1 = find_urls(w1)
            if stop in wiki1:
                return start, wiki1, stop
            else:
                for w2 in wiki1:
                    wiki2 = find_urls(w2)
                    if stop in wiki2:
                        return start, wiki1, wiki2, stop
                    else:
                        for w3 in wiki2:
                            wiki3 = find_urls(w3)
                            if stop in wiki3:
                                return start, wiki1, wiki2, wiki3, stop
out_wikilinks = []
out_wikilinks = find_out(start, stop)
for i in out_wikilinks:
    print(i)
