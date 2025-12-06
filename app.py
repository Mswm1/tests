from flask import Flask, render_template, request
import datetime
import sqlite3

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/main", methods=["GET", "POST"])
def main():
    name = request.form.get('q')
    timestamp = datetime.datetime.now()
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute('insert into user (name,timestamp) values (?,?)', (name, timestamp))
    conn.commit()
    c.close()
    conn.close()
    return render_template("main.html")


@app.route("/paynow", methods=["GET", "POST"])
def paynow():
    return render_template("paynow.html")


@app.route("/deposit", methods=["GET", "POST"])
@app.route("/userLog", methods=["GET", "POST"])
def userLog():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute('select * from user')
    r = ""
    for row in c:
        print(row)
        r = r + str(row)
    c.close()
    conn.close()
    return render_template("userLog.html", r=r)


@app.route("/deleteUserLog", methods=["GET", "POST"])
def deleteUserLog():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute('DELETE FROM user', );
    conn.commit()
    c.close()
    conn.close()
    return render_template("deleteUserLog.html")


if __name__ == "__main__":
    app.run(debug=True)
