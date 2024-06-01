# discord_chat_scraper
Scrapes specified number of recent chats from desired Discord channel

# install requirements
pip install -r requirements.txt

# scraping the messages
 -> Open the Discord Channel in your browser <br>
 -> Start Dev Tools > Network  <br>
 -> Type something in the text area of the chat, you'll notice a new header <br>
 -> Scroll to authorization, copy <br>
 -> Click on any old message on the channel you want to scrape > Copy Message Link > Copy the channel ID <br>
 ![channel ID](image.png) <br>
 -> Run python main.py <br>
 -> Proceed as directed <br>