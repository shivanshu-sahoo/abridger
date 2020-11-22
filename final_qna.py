from main_app import Question_Generation
from app_summarize_1 import *
from urllib.request import Request, urlopen
import bs4 as bs
import re


def image_to_questions(path):
    open_cv_image = cv2.imread(path)
    thres= preprocess_image(open_cv_image)
    text= pytesseract.image_to_string(thres)
    paragraphs=text
    article_text = ""
    article_text =paragraphs
    # Removing Square Brackets and Extra Spaces
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    article_text = re.sub(r'\s+', ' ', article_text)
    # Removing special characters and digits
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
    qna = Question_Generation(formatted_article_text)
    questions = [ sub["question"] for sub in qna]
    answers = [sub["answer"] for sub in qna]    
     
    return questions , answers

def url_to_questions(url):
    str1 = url
    req = Request(str1, headers={'User-Agent': 'Mozilla/5.0'})
    article= urlopen(req).read()
    parsed_article = bs.BeautifulSoup(article)
    paragraphs = parsed_article.find_all('p')
    article_text = ""
    for p in paragraphs:
        article_text +=p.text
    # Removing Square Brackets and Extra Spaces
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    article_text = re.sub(r'\s+', ' ', article_text)
    # Removing special characters and digits
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
    qna = Question_Generation(formatted_article_text)
    questions = [ sub["question"] for sub in qna]
    answers = [sub["answer"] for sub in qna]   
    
    return questions , answers

def text_to_question(text):
    qna = Question_Generation(text)
    questions = [ sub["question"] for sub in qna]
    answers = [sub["answer"] for sub in qna]   
     
    return questions , answers
    
