from nntplib import NNTP
import datetime


def connect():
    """Connects to the EPITA news server"""
    server = NNTP('news.epita.fr')
    if server is None:
        print("Error in fetching server")
        exit(-1)
    return server


def get_groups():
    """Returns a collection tuple ['group', 'last', 'first', 'flag']
    of the groups existing since i (the creator) was born"""
    server = connect()
    resp, group_tuple = server.newgroups(datetime.date(2000, 10, 5))
    group_list = []
    for group in group_tuple:
        group_list.append(group.group)
    return group_list


def get_article_list(group):
    """Returns a list of articles from a group"""
    server = connect()
    resp, articles = server.newnews(group, datetime.date(2000, 10, 5))
    return articles


def get_article(message_id):
    """Returns a string with the message content"""
    server = connect()
    resp, info = server.article(message_id)
    content = ""
    for line in info.lines:
        content += line
    print(content)
    return content
