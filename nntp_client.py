from nntplib import NNTP
import datetime


def connect():
    """Connects to the EPITA news server"""
    server = NNTP('news.epita.fr')
    if server is None:
        print("Error in fetching server")
        exit(-1)
    return server


def get_groups(server):
    """Return a collection tuple ['group', 'last', 'first', 'flag']
    of the groups existing since i was born"""
    resp, group_tuple = server.newgroups(datetime.date(2000, 10, 5))
    group_list = []
    for group in group_tuple:
        group_list.append(group.group)
    return group_list
