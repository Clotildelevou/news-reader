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
        group_list.append(group.group)
    server.quit()
    return group_list


def get_all_articles():
    """Returns a list of articles from all groups"""
    server = NNTP('news.epita.fr')
    resp, group_tuple = server.list()
    group_list = []
    article_list = [[]]
    for group in group_tuple:
        group_list.append(group.group)
        _, _, first, last, _ = server.group(group.group)
        try:
            article_list.append(server.over((first, last)))
        except nntplib.NNTPError:
            pass
    server.quit()
    return article_list


def get_group_articles(group):
    """Returns a list of articles from a group"""
    server = NNTP('news.epita.fr')
    tuple = ()
    _, _, first, last, _ = server.group(group)
    try:
        tuple = server.over((first, last))
    except nntplib.NNTPError as err:
        pass
    server.quit()
    return tuple[1]


def refresh_articles(group, last_refresh):
    """Returns a list of new articles from a group since last refresh"""
    server = NNTP('news.epita.fr')
    resp, articles = server.newnews(group, last_refresh)
    server.quit()
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
