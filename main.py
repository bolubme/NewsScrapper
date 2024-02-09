# main.py
from newsScrapers import guardian_scraper, telegraph_scraper, independent_scraper, washington_scraper, bbc_scraper, talksport_scraper



def run_all_scrapers():
    # print("Running Guardian Scraper...")
    # guardian_scraper.scrape()
    # print("Guardian Scraper Completed.\n")

    # print("Running Telegraph Scraper...")
    # telegraph_scraper.scrape()
    # print("Telegraph Scraper Completed.\n")

    # print("Running Independent Scraper...")
    # independent_scraper.scrape()
    # print("Independent Scraper Completed.\n")

    # print("Running Washingtonpost Scraper...")
    # washington_scraper.scrape()
    # print("Washingtonpost Scraper Completed.\n")

    print("Running BBC Scraper...")
    bbc_scraper.scrape()
    print("BBC Scraper Completed.\n")

    # print("Running Talk sport Scraper...")
    # talksport_scraper.scrape()
    # print("Talk sport Scraper Completed.\n")


def main():
    run_all_scrapers()


if __name__ == "__main__":
    main()
