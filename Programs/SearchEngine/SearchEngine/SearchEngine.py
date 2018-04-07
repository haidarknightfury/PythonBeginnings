#Finish crawl web
def get_page(url):
    # This is a simulated get_page procedure so that you can test your
    # code on two pages "http://xkcd.com/353" and "http://xkcd.com/554".
    # A procedure which actually grabs a page from the web will be
    # introduced in unit 4.
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return '''<html> <body> This is a test page for learning to crawl!
    <p> It is a good idea to
    <a href="http://www.udacity.com/cs101x/crawling.html">
    learn to crawl</a> before you try to
    <a href="http://www.udacity.com/cs101x/walking.html">walk</a> or
    <a href="http://www.udacity.com/cs101x/flying.html">fly</a>.</p></body>
    </html>'''

        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return '''<html> <body> I have not learned to crawl yet, but I am
    quite good at  <a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.
    </body> </html>'''

        elif url == "http://www.udacity.com/cs101x/walking.html":
            return '''<html> <body> I cant get enough
    <a href="http://www.udacity.com/cs101x/index.html">crawling</a></body></html>'''

        elif url == "http://www.udacity.com/cs101x/flying.html":
            return '''<html>
    <body>The magic words are Squeamish Ossifrage!</body></html>'''
    except:
        return ""
    return ""


def record_user_click(index, keyword, url):
    urls = lookup(index, keyword)
    if urls:
        for entry in urls:
            if entry[0] == url:
                entry[1] = entry[1]+1


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)

# def add_to_index(index, keyword, url):
#     for entry in index:
#         if entry[0] == keyword:
#             if not  url in entry[1]:
#                entry[1].append(url)
#             return
#     # not found, add new keyword to index
#     index.append([keyword, [url]])

def add_to_index(index, keyword, url):
    # format of index: [[keyword, [[url, count], [url, count],..]],...]
    for entry in index:
        if entry[0] == keyword:
            for urls in entry[1]:
                if urls[0] == url:
                    return
            entry[1].append([url,0])
            return
    # not found, add new keyword to index
    index.append([keyword, [[url,0]]])


def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)


def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def split_string(source,splitlist):
    output = []
    atSplit = True
    for char in source:
        if char in splitlist:
            atSplit = True
        else:
            if atSplit:
                output.append(char)
                atSplit= False
            else:
                output[-1] = output[-1]+char
    return output


def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    graph = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
          content = get_page(page)
          add_page_to_index(index, page, content)
          outlinks = get_all_links(content)
          union(tocrawl, outlinks)
          crawled.append(page)
    return index


index = crawl_web("http://www.udacity.com/cs101x/index.html")
print (lookup(index,"is"))