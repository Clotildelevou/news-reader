import news_ui
import nntp_client as cli


if __name__ == '__main__':
    groupes = cli.get_groups()
    cli.get_articles(groupes[0])
    exit(0)
