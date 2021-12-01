import nntp_client as cli

DICT = 1
ART_NUM = 0

if __name__ == '__main__':
    cli.save_latest_news("/home/cloture/.config/conky/latest_news.txt")
    exit(0)
