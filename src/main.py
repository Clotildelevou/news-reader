from nntplib import NNTP
import datetime


def connect():
    """Connects to the EPITA news server"""
    server = NNTP('news.epita.fr')
    if server is None:
        print("Error in fetching server")
        exit(-1)


def get_groups(server):
    """Return a collection tuple ['group', 'last', 'first', 'flag']
    of the groups existing since i was born"""
    resp, groups = server.newgroups(datetime.date(2000, 10, 5))
    print(resp)


if __name__ == '__main__':
    exit(0)
