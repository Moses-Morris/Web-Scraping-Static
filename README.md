# Web-Scraping-Static
Obtaining data using Web Scraping. Web Scraping using Beautiful Soup Library in Python. Web scraping data for use in Data Science from static websites.

**Description:** This project involves web scraping data from a website and processing it to extract specific information about products listed on the site. The extracted data includes product names, currency symbols, and prices. The project utilizes Python and libraries such as `requests` and `BeautifulSoup` for web scraping.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

Before running the code, make sure you have Python installed on your system. You can install the required libraries using the following command:

```bash
pip install requests beautifulsoup4
```

# How It Works

The project uses the `requests` library to send an HTTP request to the specified URL (`https://greenspoon.co.ke/product-category/fruit-veg/fresh-herbs/`) and fetch the webpage content.

The `BeautifulSoup` library is then used to parse the HTML content of the webpage, allowing the program to extract specific data from the HTML tags.

The program locates product containers on the webpage using their class names and iterates through these containers. For each container, it extracts the product name, currency symbol, and price.

The extracted data is then printed to the console. You can modify the script to save the data to a CSV file or perform other actions as needed.

## Dependencies

- **requests:** This library is used to send HTTP requests to the specified URL and retrieve the webpage content.
- **beautifulsoup4:** BeautifulSoup is a Python library for pulling data out of HTML and XML files. It provides Pythonic idioms for iterating, searching, and modifying the parse tree.

## Contributing

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch to work on a new feature or bug fix.
4. Make changes and commit them to your branch.
5. Push your changes to your fork on GitHub.
6. Create a pull request to merge your changes into the main repository.

## License

This project is licensed under the MIT License.
