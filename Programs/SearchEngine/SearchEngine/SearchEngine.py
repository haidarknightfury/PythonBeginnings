def get_next_target(page):
    tag = page.find('<a href=')
    start_link = page.find('"', tag) + 1
    end_link = page.find('"', start_link)
    url = page[start_link:end_link]
    return url, end_link

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print (url)
            page = page[endpos:]
        else:
            break


print_all_links('<div id="top_bin"><a href="http://udacity.com"><div id="top_content" class="width960">'
                      '<div class="udacity float-left"><a href="http://udacity.com">')
