
def Question_Generation(text):
    from pipelines import pipeline
    nlp = pipeline("question-generation")
    return(nlp(text))

text= input("Enter text")
print(Question_Generation(text))


