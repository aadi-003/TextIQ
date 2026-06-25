
from tkinter import *
from tkinter import messagebox
from mydb import *
from myapi import API
class NLPApp:
    def __init__(self):
        # self.lang_result = None
        self.dbo=Database()
        self.apio=API()
        self.root = Tk()
        self.root.title("NLP App")
        self.root.geometry("350x600")
        self.root.resizable(width=0, height=0)
        self.root.iconbitmap("Resources/pic.ico")
        self.root.configure(background="#778899")
        self.login_gui()
        self.root.mainloop()
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def login_gui(self):
        self.clear()
        heading = Label(self.root, text="NLP App",bg="#778899",fg ="white")
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label1 = Label(self.root, text="Login Here", bg="#779999", fg="white")
        label1.pack(pady=(10, 10))
        label1.configure(font=('verdana', 12))

        label1 = Label(self.root, text="Enter Email", bg="#778899", fg="white")
        label1.pack(pady=(10, 10))
        label1.configure(font=('verdana', 10))
        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root, text="Enter password", bg="#778899", fg="white")
        label2.pack(pady=(10, 10))
        label2.configure(font=('verdana', 10))
        self.password_input = Entry(self.root, width=50,show="*")
        self.password_input.pack(pady=(5, 10), ipady=4)
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_b = Button(self.root, text="Login", bg="black", fg="white",command=self.perform_login)
        login_b.pack(pady=(10, 10))
        login_b.configure(font=('verdana', 10))

        label2 = Label(self.root, text="Not a member ?", bg="#778888", fg="white")
        label2.pack(pady=(10, 10))
        register_b = Button(self.root, text="Register", bg="black", fg="white",command=self.register_gui)
        register_b.pack(pady=(10, 10))
        register_b.configure(font=('verdana', 10))

    def register_gui(self):
        self.clear()
        heading = Label(self.root, text="NLP App", bg="#778899", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label1 = Label(self.root, text="Create you new account here ", bg="#779999", fg="white")
        label1.pack(pady=(10, 10))
        label1.configure(font=('verdana', 12))

        name1= Label(self.root, text="Enter your name", bg="#778899", fg="white")
        name1.pack(pady=(10, 10))
        name1.configure(font=('verdana', 10))
        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text="Enter Email", bg="#778899", fg="white")
        label1.pack(pady=(10, 10))
        label1.configure(font=('verdana', 10))
        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text="Enter password", bg="#778899", fg="white")
        label2.pack(pady=(10, 10))
        label2.configure(font=('verdana', 10))
        self.password_input = Entry(self.root, width=50,show="*")
        self.password_input.pack(pady=(5, 10), ipady=4)
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_b = Button(self.root, text="Register", bg="black", fg="white", command=self.perform_registration)
        login_b.pack(pady=(10, 10))
        login_b.configure(font=('verdana', 10))

        label2 = Label(self.root, text="Already a member ?", bg="#778888", fg="white")
        label2.pack(pady=(10, 10))
        register_b = Button(self.root, text="Login", bg="black", fg="white", command=self.login_gui)
        register_b.pack(pady=(10, 10))
        register_b.configure(font=('verdana', 10))

    def perform_registration(self):
        name=self.name_input.get()
        email=self.email_input.get()
        password=self.password_input.get()
        response = self.dbo.add_data(name,email,password)
        if response:
            messagebox.showinfo(message="Registration Successful", title="Success")
            self.login_gui()
        else:
            messagebox.showerror('error','Email already exists')


    def perform_login(self):
        email=self.email_input.get()
        password=self.password_input.get()
        checkf=self.dbo.check_data(email,password)
        if checkf==2:
            messagebox.showinfo(message="Login Successful", title="Success")
            self.main_page_gui()
        elif checkf==0:
            messagebox.showerror('error','Email does not exist, Please register first.')
        else:
            messagebox.showerror('error','Password Incorrect, Try Again.')

    def main_page_gui(self):
        self.clear()
        sentiment_b = Button(self.root, text="Sentiment Analysis", fg="black", bg="white",width=30,height=4, command=self.sentiment_gui)
        sentiment_b.configure(font=('verdana', 12))
        sentiment_b.pack(pady=(10, 10))

        ner_b = Button(self.root, text="Text Similarity", fg="black", bg="white", width=30,height=4, command=self.ner_gui)
        ner_b.configure(font=('verdana', 12))
        ner_b.pack(pady=(10, 10))

        lang_b = Button(self.root, text="Language Detection", fg="black", bg="white", width=30,height=4, command=self.language_gui)
        lang_b.configure(font=('verdana', 12))
        lang_b.pack(pady=(10, 10))

        logout = Button(self.root, text="Log Out", fg="black", bg="white", width=17, height=1,
                        command=self.login_gui)
        logout.configure(font=('verdana', 8))
        logout.pack(pady=(5, 10))

    def sentiment_gui(self):
        self.clear()
        heading = Label(self.root, text="Sentiment Analysis", bg="#9e9e9e", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 19, 'bold'))


        text= Label(self.root, text="Enter text", bg="#778899", fg="white")
        text.pack(pady=(10, 10))
        text.configure(font=('verdana', 10))
        self.text_input = Entry(self.root, width=50)
        self.text_input.pack(pady=(5, 10), ipady=4)

        analyse = Button(self.root, text="Analyse sentiment", fg="black", bg="white", width=20, height=2,
                        command=self.do_sentiment_analysis)
        analyse.configure(font=('verdana',10))
        analyse.pack(pady=(5, 10))

        self.senti_result = Button(self.root, text='', fg="black", bg="#778899")
        self.senti_result.configure(font=('verdana', 16))
        self.senti_result.pack(pady=(10, 10))

        back = Button(self.root, text="Go Back", fg="black", bg="white", width=17, height=1,
                      command=self.main_page_gui)
        back.configure(font=('verdana', 8))
        back.pack(pady=(5, 10))

    def do_sentiment_analysis(self):
        text = self.text_input.get()
        result = self.apio.sentiment_analysis(text)
        txt=''
        txt =txt +  result['sentiment'] + '--> ' + str(result['score']) + '\n'
        self.senti_result['text'] = txt
        # print(f"Sentiment: {result['sentiment']}")
        # print(f"Score:     {result['score']}")

    def ner_gui(self):
        self.clear()
        heading = Label(self.root, text="Text Similarity Check", bg="#9e9e9e", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 17, 'bold'))

        text = Label(self.root, text="Enter first text ", bg="#778899", fg="white")
        text.pack(pady=(10, 10))
        text.configure(font=('verdana', 10))
        self.text_input = Entry(self.root, width=50)
        self.text_input.pack(pady=(5, 10), ipady=4)

        text2 = Label(self.root, text="Enter second text ", bg="#778899", fg="white")
        text2.pack(pady=(10, 10))
        text2.configure(font=('verdana', 10))
        self.text2_input = Entry(self.root, width=50)
        self.text2_input.pack(pady=(5, 10), ipady=4)

        analyse_t = Button(self.root, text="Analyse text", fg="black", bg="white", width=20, height=2,
                         command=self.do_text_analysis)
        analyse_t.configure(font=('verdana', 10))
        analyse_t.pack(pady=(5, 10))

        self.ner_result = Button(self.root, text='', fg="black", bg="#778899")
        self.ner_result.configure(font=('verdana', 12))
        self.ner_result.pack(pady=(10, 10))

        back_m = Button(self.root, text="Go Back", fg="black", bg="white", width=17, height=1,command=self.main_page_gui)
        back_m.configure(font=('verdana', 8))
        back_m.pack(pady=(5, 10))

    def do_text_analysis(self):
        text = self.text_input.get()
        text2 = self.text2_input.get()
        result = self.apio.text_analysis(text,text2)
        txt = "similarity"  + '--> ' + str(result['similarity']) + '\n'
        self.ner_result['text'] = txt

    def language_gui(self):
        self.clear()
        heading = Label(self.root, text="Language Detection", bg="#9e9e9e", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 19, 'bold'))

        heading = Label(self.root, text="Detect among 50 languages", bg="#9e9e9e", fg="white")
        heading.pack(pady=(14,14))
        heading.configure(font=('verdana', 10, 'bold'))

        text = Label(self.root, text="Enter text", bg="#778899", fg="white")
        text.pack(pady=(10, 10))
        text.configure(font=('verdana', 10))
        self.text_input = Entry(self.root, width=50)
        self.text_input.pack(pady=(5, 10), ipady=4)

        analyse = Button(self.root, text="Detect Language", fg="black", bg="white", width=20, height=2,
                         command=self.do_lang_analysis)
        analyse.configure(font=('verdana', 10))
        analyse.pack(pady=(5, 10))

        self.lang_result = Button(self.root, text='', fg="black", bg="#778899")
        self.lang_result.configure(font=('verdana', 13))
        self.lang_result.pack(pady=(10, 10))


        back = Button(self.root, text="Go Back", fg="black", bg="white", width=17, height=1,
                        command=self.main_page_gui)
        back.configure(font=('verdana', 8))
        back.pack(pady=(5, 10))

    def do_lang_analysis(self):
        pass
        text = self.text_input.get()
        result = self.apio.language_analysis(text)
        txt = ''
        txt = txt +'language --> '+ str(result['language']) + '\n'
        self.lang_result['text'] = txt





nlp=NLPApp()