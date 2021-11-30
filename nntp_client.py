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


def get_article_content(group, message_id):
    """Returns a string with the message content"""
    server = NNTP('news.epita.fr')
    tuple = ()
    _, _, first, last, _ = server.group(group)
    try:
        tuple = server.over((first, last))
    except nntplib.NNTPError as err:
        pass
    _, info_head = server.head(message_id)
    _, info_body = server.body(message_id)
    head = ""
    body = ""
    for line in info_head.lines:
        head += line.decode('UTF-8') + "\n"
    for line in info_body.lines:
        body += line.decode('UTF-8') + "\n"
    print(colors.OKGREEN + "Group articles fetched !" + colors.ENDC)
    server.quit()
    return head, body



