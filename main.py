import os
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
from app_summarize_1 import summarize_image, summarize_url, summarize_para
from flask_wtf.csrf import CSRFProtect
from qna_dummy import qna, check_answer
#from dotenv import load_dotenv
from final_qna import *

#load_dotenv()

#SECRET_KEY = os.getenv("SECRET_KEY")
UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

app.config['SECRET_KEY'] = "1234"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
csrf = CSRFProtect(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image', methods=['GET', 'POST'])
def upload_image():

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            path_clean="./static/uploads/{}".format(filename)
            """
            text=summarize_image(path_clean) 
            qnas,ans=text_to_question(text) 
            qa=zip(qnas,ans)
            #qnas,ans=qna(text) 
            #qa=zip(qnas,ans)
            """         
             
            print("File is saved successfully in the uploads folder!!",path_clean)
            return render_template('image_input.html',upload=True,fname=file.filename,text=text,qa=qa)
    return render_template('image_input.html')

@app.route('/text', methods=['GET','POST'])
def text():
    if request.method == 'POST':
        raw_text=request.form['raw_text']
       
        if raw_text == '':
            flash('No text entered')
            return redirect(request.url) 
        """  
        else:   
             try: 
                request.form['gen']=="generate"
                qnas , ans = text_to_question(raw_text)  
                qa = zip(qnas,ans) 
                #qnas,ans=qna(text) 
                #qa=zip(qnas,ans)   
                print(qa)    
                return render_template('text_input.html',output_gen=True,qa=qa)  
               
             except:
                pass

             try: 
                request.form['sum']=="summarize"
                print("gen")
                summarized_text= summarize_para(raw_text)
                return render_template('text_input.html',output_sum=True,summarized_text=summarized_text) 
             except:
                pass    
        """
           
    return render_template('text_input.html')


@app.route('/url', methods=['GET','POST'])
def url():
    if request.method == 'POST':
        url_text=request.form['url_text']
        if url == '':
            flash('No URL entered')
            return redirect(request.url)
        """
        else:   
             try: 
                request.form['gen']=="generate"
                qnas,ans=url_to_questions(url_text)
                qa=zip(qnas,ans)
                #qnas,ans=qna(text) 
                #qa=zip(qnas,ans) 
                return render_template('url_input.html',output_gen=True,qa=qa)  
             except:
                pass

             try: 
                request.form['sum']=="summarize"
                summarized_text= summarize_url(url_text)
                return render_template('url_input.html',output_sum=True,summarized_text=summarized_text)
             except:
                pass  
        """
           
    return render_template('url_input.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1" , port=8080 ,  debug=True)    