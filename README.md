# PCLUB
A web scraper that prints the name, organisation and project from https://summerofcode.withgoogle.com/archive/2019/projects/. Also includes validation with a local JSON file.

# SETUP
If you don't have requests,csv,json or beautifulsoul install those libraries by using apt-get (for ubuntu or debian distributions) or just use good ol' pip.
pip install requests
pip install beautifulsoup4

Also ensure you have python 2.7 or higher installed.

# RUN
Clone the repository and switch to it in the terminal.
Run python scraping.py and then python scraping2.py from the terminal.
scraping.py creates an output.csv file.
scraping2.py then uses the same csv file and students.json to run some validation tests.

