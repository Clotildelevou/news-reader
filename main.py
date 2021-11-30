import nntp_client as cli

DICT = 1
ART_NUM = 0

if __name__ == '__main__':
    group_index = 1
    news_index = 0
    groups = cli.get_groups()
    art_list = cli.get_group_articles(groups[group_index])
    cli.pretty_print_article(groups[group_index], art_list[news_index][DICT]['message-id'])
    exit(0)
