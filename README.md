# Steam Game Data Scraper
This project uses the Scrapy framework to scrape data from the Steam store website. The scraped data includes information about various games available on Steam and is saved in a JSON file.

### Overview
The primary goal of this project is to demonstrate data collection skills using Python and Scrapy. The extracted data includes key information about games on the Steam platform, which can be used for further analysis.

### Scraped Data
The columns included in the scraped data are:

- discount: The discount percentage for the game.
- discounted_price: The price of the game after discount.
- game_name: The name of the game.
- game_url: The URL to the game's Steam page.
- original_price: The original price of the game before discount.
- release_date: The release date of the game.
- review_data: Detailed review data including the number of reviews and the overall rating.
- reviews_summary: A summary of the game's reviews.

  
### Project Structure
- steam_game_data_scraper/: The main project directory.
- spiders/: Contains the Scrapy spider for scraping data from Steam.
- items.py: Defines the items to be scraped.
- pipelines.py: Defines the pipelines for processing scraped data.
- settings.py: Contains project settings for Scrapy.
