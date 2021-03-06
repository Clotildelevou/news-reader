import os
from datetime import date, timedelta
from nntplib import NNTP
import nntplib
from colors import colors


def get_groups():
    """Returns a collection tuple ['group', 'last', 'first', 'flag']
    of the groups existing since i (the creator) was born"""
    server = NNTP('news.epita.fr')
    resp, group_tuple = server.list()
    group_list = []
    for group in group_tuple:
        group_list.append(group)
    return group_list


def get_all_articles():
    """Returns a list of articles from all groups"""
    server = NNTP('news.epita.fr')
    resp, group_tuple = server.list()
    group_list = []
    article_list = [[]]
    for group in group_tuple:
        group_list.append(group)
        _, _, first, last, _ = server.group(group)
        try:
            article_list.append(server.over((first, last)))
        except nntplib.NNTPError:
            pass
    return article_list


def get_group_articles(group):
    """Returns a list of articles from a group"""
    server = NNTP('news.epita.fr')
    over = ()
    _, _, first, last, _ = server.group(group)
    try:
        over = server.over((first, last))
    except nntplib.NNTPError as err:
        pass
    return over[1]


def refresh_articles(group, last_refresh):
    """Returns a list of new articles from a group since last refresh"""
    server = NNTP('news.epita.fr')
    resp, articles = server.newnews(group, last_refresh)
    return articles


def get_article_content(group, message_id):
    """Returns a string with the message content"""
    server = NNTP('news.epita.fr')
    _, _, first, last, _ = server.group(group)
    _, _ = server.over((first, last))
    _, info_head = server.head(message_id)
    _, info_body = server.body(message_id)
    head = {}
    body = ""
    for line in info_head.lines:
        entry = (nntplib.decode_header(line.decode('UTF-8')).split(": "))
        if len(entry) == 2:
            head[entry[0]] = entry[1]
    for line in info_body.lines:
        body += (nntplib.decode_header(line.decode('UTF-8')))
    if len(body) > 1024:
        body = body[0:1024] + "...\n"
    return head, body


def pretty_print_article(group, message_id):
    """Pretty prints the body of an article"""
    server = NNTP('news.epita.fr')
    server.group(group)
    head, body = get_article_content(group, message_id)
    print(colors.BOLD + head['Subject'] + colors.ENDC)
    print(body)
    print(colors.BOLD + head['From'] + colors.ENDC)


def pretty_print_ow(group, message_id):
    """Pretty prints the overview of an article"""
    server = NNTP('news.epita.fr')
    server.group(group)
    head, body = get_article_content(group, message_id)
    print(head['Subject'])
    print(head['From'])
    print(head['Date'] + "\n")


def save_latest_news(path):
    """Pretty prints news data in a file the news in selected groups"""
    if os.path.exists(path):
        append_write = 'a+'
    else:
        append_write = 'w+'
    file = open(path, append_write)
    server = NNTP('news.epita.fr')

    resp, group_tuple = server.list()
    group_list = []
    for group in group_tuple:
        group_list.append(group[0])

    for group in group_list[0:len(group_list) - 1]:
        resp, articles = server.newnews(group, date.today() - timedelta(days=1))
        for article in articles:
            head, body = get_article_content(group, article)
            if 'Subject' in head and 'From' in head:
                file.write(head['Subject'] + "\n" + head['From'] + "\n" + body + "\n\n")
    file.close()
