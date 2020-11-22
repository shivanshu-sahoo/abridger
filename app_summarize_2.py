import streamlit as st
from main_app import Question_Generation
from GET_URL import get_url
from GET_IMAGE import get_img


def app():
    
    def Question_Answer(qna):
        user_answer = ["i"] 
        questions = [ sub["question"] for sub in qna]
        answers = [sub["answer"] for sub in qna]    
        if len(questions) == 1:
            st.write(questions[0])
            user_answer_1 = st.text_area("Enter the Answer:",height=2 , key = 1)
            submission = st.button("Submit" , key = 1)
            if submission:
                user_answer.append(user_answer_1)
                user_answer.pop(0)
                correct_wrong = get_similarity([answers[0]] , user_answer)
                total_marks = (sum(correct_wrong)/len(correct_wrong)) * 100
                st.write("Awesome!!!" , str(total_marks))
            if 0 in correct_wrong:
                st.write("You have done some mistakes, here is where you went wrong...")
                for boolean in correct_wrong:
                    if boolean == 0:
                        st.write("Mistaken Question:" , questions[0])
                        st.write("Correct answer: " , answers[0])
                    else:
                        pass
            else:
                st.balloons()
            
                    
        
            
        elif len(questions) == 2:
            st.write(questions[0])
            user_answer_1 = st.text_area("Enter the Answer:",height=2 , key = 1)
            st.write(questions[1])
            user_answer_2 = st.text_area("Enter the Answer:",height=2 , key = 2)
            submission = st.button("Submit" , key = 1)
            if submission:
                user_answer.extend([user_answer_1 , user_answer_2])
                user_answer.pop(0)
                correct_wrong = get_similarity(answers , user_answer)
                total_marks = (sum(correct_wrong)/len(correct_wrong)) * 100
                st.write("Awesome!!!" , str(total_marks))
            i=0
            if 0 in correct_wrong:
                st.write("You have done some mistakes, here is where you went wrong...")
                for i in range(len(correct_wrong)):
                    if correct_wrong[i] == 0:
                        st.write("Mistaken Question:" , questions[i])
                        st.write("Correct answer: " , answers[i])
                    else:
                        pass
            else:
                st.balloons()
        
                    
        elif len(questions) == 3:
            st.write(questions[0])
            user_answer_1 = st.text_area("Enter the Answer:",height=2 , key = 1)
            st.write(questions[1])
            user_answer_2 = st.text_area("Enter the Answer:",height=2 , key = 2)
            st.write(questions[2])
            user_answer_3 = st.text_area("Enter the Answer:",height=2 , key = 3)
            submission = st.button("Submit" , key = 1)
            if submission:
                user_answer.extend([user_answer_1 , user_answer_2 , user_answer_3])
                user_answer.pop(0)
                correct_wrong = get_similarity(answers , user_answer)
                total_marks = (sum(correct_wrong)/len(correct_wrong)) * 100
                st.write("Awesome!!!" , str(total_marks))
            i=0
            if 0 in correct_wrong:
                st.write("You have done some mistakes, here is where you went wrong...")
                for i in range(len(correct_wrong)):
                    if correct_wrong[i] == 0:
                        st.write("Mistaken Question:" , questions[i])
                        st.write("Correct answer: " , answers[i])
                    else:
                        pass
            else:
                st.balloons()
        
        
        elif len(questions) == 4:
            st.write(questions[0])
            user_answer_1 = st.text_area("Enter the Answer:",height=2 , key = 1)
            st.write(questions[1])
            user_answer_2 = st.text_area("Enter the Answer:",height=2 , key = 2)
            st.write(questions[2])
            user_answer_3 = st.text_area("Enter the Answer:",height=2 , key = 3)
            st.write(questions[3])
            user_answer_4 = st.text_area("Enter the Answer:",height=2 , key = 4)
            submission = st.button("Submit" , key = 1)
            if submission:
                user_answer.extend([user_answer_1 , user_answer_2 , user_answer_3 , user_answer_4])
                user_answer.pop(0)
                correct_wrong = get_similarity(answers , user_answer)
                total_marks = (sum(correct_wrong)/len(correct_wrong)) * 100
                st.write("Awesome!!!" , str(total_marks))
            i=0
            if 0 in correct_wrong:
                st.write("You have done some mistakes, here is where you went wrong...")
                for i in range(len(correct_wrong)):
                    if correct_wrong[i] == 0:
                        st.write("Mistaken Question:" , questions[i])
                        st.write("Correct answer: " , answers[i])
                    else:
                        pass
            else:
                st.balloons()
            
        elif len(questions) == 5:
            st.write(questions[0])
            user_answer_1 = st.text_area("Enter the Answer:",height=2 , key = 1)
            st.write(questions[1])
            user_answer_2 = st.text_area("Enter the Answer:",height=2 , key = 2)
            st.write(questions[2])
            user_answer_3 = st.text_area("Enter the Answer:",height=2 , key = 3)
            st.write(questions[3])
            user_answer_4 = st.text_area("Enter the Answer:",height=2 , key = 4)
            st.write(questions[4])
            user_answer_5 = st.text_area("Enter the Answer:",height=2 , key = 5)
            submission = st.button("Submit" , key = 1)
            if submission:
                user_answer.extend([user_answer_1 , user_answer_2 , user_answer_3 , user_answer_4 , user_answer_5])
                user_answer.pop(0)
                correct_wrong = get_similarity(answers , user_answer)
                total_marks = (sum(correct_wrong)/len(correct_wrong)) * 100
                st.write("Awesome!!!" , str(total_marks))
            i=0
            if 0 in correct_wrong:
                st.write("You have done some mistakes, here is where you went wrong...")
                for i in range(len(correct_wrong)):
                    if correct_wrong[i] == 0:
                        st.write("Mistaken Question:" , questions[i])
                        st.write("Correct answer: " , answers[i])
                    else:
                        pass
            else:
                st.balloons()
                    
        elif len(questions) == 6:
            st.write(questions[0])
            user_answer_1 = st.text_area("Enter the Answer:",height=2 , key = 1)
            st.write(questions[1])
            user_answer_2 = st.text_area("Enter the Answer:",height=2 , key = 2)
            st.write(questions[2])
            user_answer_3 = st.text_area("Enter the Answer:",height=2 , key = 3)
            st.write(questions[3])
            user_answer_4 = st.text_area("Enter the Answer:",height=2 , key = 4)
            st.write(questions[4])
            user_answer_5 = st.text_area("Enter the Answer:",height=2 , key = 5)
            st.write(questions[5])
            user_answer_6 = st.text_area("Enter the Answer:",height=2 , key = 6)
            submission = st.button("Submit" , key = 1)
            if submission:
                user_answer.extend([user_answer_1 , user_answer_2 , user_answer_3 , user_answer_4 , user_answer_5 , user_answer_6])
                user_answer.pop(0)
                correct_wrong = get_similarity(answers , user_answer)
                total_marks = (sum(correct_wrong)/len(correct_wrong)) * 100
                st.write("Awesome!!!" , str(total_marks))
            i=0
            if 0 in correct_wrong:
                st.write("You have done some mistakes, here is where you went wrong...")
                for i in range(len(correct_wrong)):
                    if correct_wrong[i] == 0:
                        st.write("Mistaken Question:" , questions[i])
                        st.write("Correct answer: " , answers[i])
                    else:
                        pass
            else:
                st.balloons()
                    
        elif len(questions) == 7:
            st.write(questions[0])
            user_answer_1 = st.text_area("Enter the Answer:",height=2 , key = 1)
            st.write(questions[1])
            user_answer_2 = st.text_area("Enter the Answer:",height=2 , key = 2)
            st.write(questions[2])
            user_answer_3 = st.text_area("Enter the Answer:",height=2 , key = 3)
            st.write(questions[3])
            user_answer_4 = st.text_area("Enter the Answer:",height=2 , key = 4)
            st.write(questions[4])
            user_answer_5 = st.text_area("Enter the Answer:",height=2 , key = 5)
            st.write(questions[5])
            user_answer_6 = st.text_area("Enter the Answer:",height=2 , key = 6)
            st.write(questions[6])
            user_answer_7 = st.text_area("Enter the Answer:",height=2 , key = 7)
            submission = st.button("Submit" , key = 1)
            if submission:
                user_answer.extend([user_answer_1 , user_answer_2 , user_answer_3 , user_answer_4 , user_answer_5 , user_answer_6 , user_answer_7])
                user_answer.pop(0)
                correct_wrong = get_similarity(answers , user_answer)
                total_marks = (sum(correct_wrong)/len(correct_wrong)) * 100
                st.write("Awesome!!!" , str(total_marks))
            i=0
            if 0 in correct_wrong:
                st.write("You have done some mistakes, here is where you went wrong...")
                for i in range(len(correct_wrong)):
                    if correct_wrong[i] == 0:
                        st.write("Mistaken Question:" , questions[i])
                        st.write("Correct answer: " , answers[i])
                    else:
                        pass
            else:
                st.balloons()
                    
        elif len(questions) == 8:
            st.write(questions[0])
            user_answer_1 = st.text_area("Enter the Answer:",height=2 , key = 1)
            st.write(questions[1])
            user_answer_2 = st.text_area("Enter the Answer:",height=2 , key = 2)
            st.write(questions[2])
            user_answer_3 = st.text_area("Enter the Answer:",height=2 , key = 3)
            st.write(questions[3])
            user_answer_4 = st.text_area("Enter the Answer:",height=2 , key = 4)
            st.write(questions[4])
            user_answer_5 = st.text_area("Enter the Answer:",height=2 , key = 5)
            st.write(questions[5])
            user_answer_6 = st.text_area("Enter the Answer:",height=2 , key = 6)
            st.write(questions[6])
            user_answer_7 = st.text_area("Enter the Answer:",height=2 , key = 7)
            st.write(questions[7])
            user_answer_8 = st.text_area("Enter the Answer:",height=2 , key = 8)
            submission = st.button("Submit" , key = 1)
            if submission:
                user_answer.extend([user_answer_1 , user_answer_2 , user_answer_3 , user_answer_4 , user_answer_5 , user_answer_6 , user_answer_7 , user_answer_8])
                user_answer.pop(0)
                correct_wrong = get_similarity(answers , user_answer)
                total_marks = (sum(correct_wrong)/len(correct_wrong)) * 100
                st.write(total_marks)
            i=0
            if 0 in correct_wrong:
                st.write("You have done some mistakes, here is where you went wrong...")
                for i in range(len(correct_wrong)):
                    if correct_wrong[i] == 0:
                        st.write("Mistaken Question:" , questions[i])
                        st.write("Correct answer: " , answers[i])
                    else:
                        pass
            else:
                st.balloons()
                    
        elif len(questions) == 9:
            st.write(questions[0])
            user_answer_1 = st.text_area("Enter the Answer:",height=2 , key = 1)
            st.write(questions[1])
            user_answer_2 = st.text_area("Enter the Answer:",height=2 , key = 2)
            st.write(questions[2])
            user_answer_3 = st.text_area("Enter the Answer:",height=2 , key = 3)
            st.write(questions[3])
            user_answer_4 = st.text_area("Enter the Answer:",height=2 , key = 4)
            st.write(questions[4])
            user_answer_5 = st.text_area("Enter the Answer:",height=2 , key = 5)
            st.write(questions[5])
            user_answer_6 = st.text_area("Enter the Answer:",height=2 , key = 6)
            st.write(questions[6])
            user_answer_7 = st.text_area("Enter the Answer:",height=2 , key = 7)
            st.write(questions[7])
            user_answer_8 = st.text_area("Enter the Answer:",height=2 , key = 8)
            st.write(questions[8])
            user_answer_9 = st.text_area("Enter the Answer:",height=2 , key = 9)
            submission = st.button("Submit" , key = 1)
            if submission:
                user_answer.extend([user_answer_1 , user_answer_2 , user_answer_3 , user_answer_4 , user_answer_5 , user_answer_6 , user_answer_7 , user_answer_8 , user_answer_9])
                user_answer.pop(0)
                correct_wrong = get_similarity(answers , user_answer)
                total_marks = (sum(correct_wrong)/len(correct_wrong)) * 100
                st.write("Awesome!!!" , str(total_marks))
            i=0
            if 0 in correct_wrong:
                st.write("You have done some mistakes, here is where you went wrong...")
                for i in range(len(correct_wrong)):
                    if correct_wrong[i] == 0:
                        st.write("Mistaken Question:" , questions[i])
                        st.write("Correct answer: " , answers[i])
                    else:
                        pass
            else:
                st.balloons()
                    
        elif len(questions) >= 10:
            st.write(questions[0])
            user_answer_1 = st.text_area("Enter the Answer:",height=2 , key = 1)
            st.write(questions[1])
            user_answer_2 = st.text_area("Enter the Answer:",height=2 , key = 2)
            st.write(questions[2])
            user_answer_3 = st.text_area("Enter the Answer:",height=2 , key = 3)
            st.write(questions[3])
            user_answer_4 = st.text_area("Enter the Answer:",height=2 , key = 4)
            st.write(questions[4])
            user_answer_5 = st.text_area("Enter the Answer:",height=2 , key = 5)
            st.write(questions[5])
            user_answer_6 = st.text_area("Enter the Answer:",height=2 , key = 6)
            st.write(questions[6])
            user_answer_7 = st.text_area("Enter the Answer:",height=2 , key = 7)
            st.write(questions[7])
            user_answer_8 = st.text_area("Enter the Answer:",height=2 , key = 8)
            st.write(questions[8])
            user_answer_9 = st.text_area("Enter the Answer:",height=2 , key = 9)
            st.write(questions[9])
            user_answer_10 = st.text_area("Enter the Answer:",height=2 , key = 10)
            submission = st.button("Submit" , key = 1)
            if submission:
                user_answer.extend([user_answer_1 , user_answer_2 , user_answer_3 , user_answer_4 , user_answer_5 , user_answer_6 , user_answer_7 , user_answer_8 , user_answer_9 , user_answer_10])
                user_answer.pop(0)
                correct_wrong = get_similarity(answers , user_answer)
                total_marks = (sum(correct_wrong)/len(correct_wrong)) * 100
                st.write("Awesome!!!" , str(total_marks))
            i=0
            if 0 in correct_wrong:
                st.write("You have done some mistakes, here is where you went wrong...")
                for i in range(len(correct_wrong)):
                    if correct_wrong[i] == 0:
                        st.write("Mistaken Question:" , questions[i])
                        st.write("Correct answer: " , answers[i])
                    else:
                        pass
            else:
                st.balloons()
                
    from text_similarity import get_similarity

    @st.cache(suppress_st_warning=True , allow_output_mutation = True)
    def call_question_gen(text):
        qna = Question_Generation(text)
        return qna
        
            

        
    st.title('Question Answers')
    choice=st.selectbox('How do you want to enter data to generate quiz.',('Image','URL','Text'))
        
    if(choice=='Text'):
        text = st.text_input("Enter the text")
        try:
            qna = call_question_gen(text)
            Question_Answer(qna)
        except:
            pass
        
    elif(choice == "URL"):
        try:
            URL= st.text_input('Enter the URL ',max_chars=200)
            text = get_url(URL)
            qna = call_question_gen(text)
            Question_Answer(qna)
        except:
            pass
        
    elif(choice == "Image"):
        text = get_img()
        try:
            qna = call_question_gen(text)
            Question_Answer(qna)
        except:
            pass
        