from scrapegen import  CompaniesInfo, ScrapeConfig , ScrapeGen


def main():
    # Create custom configuration
    config = ScrapeConfig(
        max_pages=30,
        max_depth=2,
        timeout=45,
        headers={"Custom-Header": "Value"}
    )

    # Initialize with custom config
    scraper = ScrapeGen(
        api_key="your-google-api-key",
        model="gemini-1.5-pro",
        config=config
    )

    urls = [
        "https://example1.com",
        "https://example2.com"
    ]

    for url in urls:
        try:
            data = scraper.scrape(url, CompaniesInfo)
            print(f"\nResults from {url}:")
            for company in data.companies:
                print(f"Found company: {company.company_name}")
        except Exception as e:
            print(f"Error processing {url}: {str(e)}")
            continue

if __name__ == "__main__":
    main()