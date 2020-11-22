from urllib.request import Request, urlopen
import bs4 as bs
import re
def get_url(url):
    str1=url
    req = Request(str1, headers={'User-Agent': 'Mozilla/5.0'})
    article= urlopen(req).read()
        
    parsed_article = bs.BeautifulSoup(article)
    paragraphs = parsed_article.find_all('p')
    
    #print(paragraphs)
        
    article_text = ""
        
    for p in paragraphs:
            article_text +=p.text
        
    # Removing Square Brackets and Extra Spaces
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    article_text = re.sub(r'\s+', ' ', article_text)
    # Removing special characters and digits
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
    
    return formatted_article_text