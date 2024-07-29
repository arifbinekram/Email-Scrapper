# Email Scrapper

Email Scrapper is a Python-based tool for extracting email addresses from a list of URLs. The script reads URLs from a file, scrapes the web pages for email addresses, and saves the results to an output file.

## Features

- Extracts email addresses from web pages.
- Supports random sleep intervals to avoid getting blocked by websites.
- Easy to use and configure.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/arifbinekram/Email-Scrapper.git
    cd Email-Scrapper
    ```

2. Install any necessary libraries:

    ```bash
    pip install urllib3
    ```

## Usage

1. Create a file named `urls.txt` in the root directory of the project and add the list of URLs to be scraped, one per line.

2. Run the script:

    ```bash
    python3 email_scraper.py
    ```

3. The results will be saved in `emails.txt` in the same directory.

### Example

Here is an example of how your `urls.txt` file might look:

```
https://www.wikipedia.org
https://www.google.com
https://www.facebook.com
https://www.youtube.com
...
```

### Output

The output file `emails.txt` will contain the URLs and the extracted email addresses, like this:

```
https://www.example.com
contact@example.com
info@example.com
https://www.anotherexample.com
support@anotherexample.com
admin@anotherexample.com
...
```

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

---

Feel free to modify this README as needed.
