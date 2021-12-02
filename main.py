from datetime import date, timedelta
import sys
import nntp_client as cli

if __name__ == '__main__':
    groups = cli.select_groups()
    print(groups)
    cli.save_latest_news("/home/cloture/.config/conky/latest_news.txt", groups)
    exit(0)
