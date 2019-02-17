from flask import Flask, render_template, request

app = Flask(__name__)

isim = []
eposta = []
konu = []
mesaj = []

@app.route("/")
def index():
	return render_template ("index.html")

@app.route("/Anasayfa")
def main():
	return render_template ("index.html")

@app.route("/İletişim",methods = ["GET","POST"])
def contact():
	if request.method == "POST":
		name = request.form.get("name")
		mail = request.form.get("mail")
		subject = request.form.get("subject")
		message = request.form.get("message")
		isim.append(name)
		eposta.append(mail)
		konu.append(subject)
		mesaj.append(message)
		return render_template ("contact.html", isim = isim,eposta = eposta, konu = konu, mesaj = mesaj)
	else:
		return render_template ("contact.html")

@app.route("/Hakkımda")
def abaut_me():
	return render_template ("about_me.html")

@app.route("/Çalışmalarım")
def my_project():
	return render_template ("my_project.html")

@app.route("/Konular")
def subject():
	return render_template ("subject.html")

@app.route("/SonYazılarım")
def last_news():
	return render_template ("last_news.html")


if __name__ == "__main__":
	app.run(debug = True)