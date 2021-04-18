# Readme scraper.py

## Open Ubuntu terminal

## 1. Install python3 if it is not already active
   sudo apt install python3

## 2. Install pip3 for python - this way we can import the necessary packages
   sudo apt install python3-pip

## 3. Install beautifulsoup4
   pip3 install bs4

## 4. Install pandas
   pip3 install pandas

## 5.Install regex
   pip3 install regex 

## 6. Open the scraper.py script (script will continue to scrape until scraper.py is stopped)
   >python3 scraper.py

##Uitleg werking scraper:
1. I sent a get request to https://www.blockchain.com/btc/unconfirmed-transactions via the request package.
2. I created a beautifulsoup item with the answer from the get request in it. Via beautifulsoup this html page will be easier to read.
3. Afterwards I use the soup.find method to get the 'class' from the html where the full data (Hash,Time,Amount (BTC), Amount (USD)) about the bitcoin tranactions is located.
4. Afterwards I use get_text to display these search results as text. 
5. I then tried to clarify the data and give it structure. So that it is easy to read and that I can ouput the data into a csv file (For example the data in the first row is seen as csv titles and all columns are split with a comma.
6. I print this data (line by line) into a new file called blockchain.csv.
7. Then I read this table again and clean it further (e.g. AMOUNT (BTC) should not appear in front of each value). This way the data is easy to read.
8. I sort the table according to the highest Amount. 
9. Then I only display the first row (highest) with .head(1).
10. Then I print this output and save the highest value as hoogste.csv for further processing in a database.
12. Afterwards I created a loop so that the above function is executed again every 60 seconds.
