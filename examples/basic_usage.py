from scrapegen import ScrapeGen, CompaniesInfo

def main():
    # Initialize ScrapeGen with your API key
    scraper = ScrapeGen(
        api_key="your-google-api-key",
        model="gemini-1.5-pro"
    )

    # Define target URL
    url = "https://example.com"

    try:
        # Scrape and extract company information
        companies_data = scraper.scrape(url, CompaniesInfo)
        
        # Print results
        for company in companies_data.companies:
            print(f"\nCompany Name: {company.company_name}")
            print(f"Description: {company.company_description}")
            print(f"Funding: {company.funding_amount}")
            print(f"CEO: {company.ceo_name}")
            print(f"URL: {company.company_url}")
            
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()
