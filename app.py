from flask import Flask,render_template,request,url_for,redirect
#import sqlite3
#conn = sqlite3.connect('books.db')
#print ("Database sucessfully opened")
#conn.execute('CREATE TABLE details (id PRIMARY KEY INT NOT NULL book_name TEXT NOT NULL,book_author TEXT NOT NULL,best_seller INT NOT NULL,book_time INT NOT NULL,book_type TEXT NOT NULL)')
#print("Table created sucessfully")
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')
@app.route('/fantasy',methods = ['GET','POST'])
def fantasy():
    if request.method=='POST':
        return redirect(url_for('index'))
    return render_template('fantasy.html')
@app.route('/fiction',methods = ['GET','POST'])
def fiction():
    if request.method=='POST':
        return redirect(url_for('index'))
    return render_template('fiction.html')
@app.route('/horror',methods = ['GET','POST'])
def horror():
    if request.method=='POST':
        return redirect(url_for('index'))
    return render_template('horror.html')
@app.route('/forms',methods = ['GET','POST'])
def forms():
    if request.method=='POST':
        return redirect(url_for('index'))
    return render_template('forms.html')
#@app.route(errorhandler(400))
if __name__ == '__main__':
    app.run(debug=True)
