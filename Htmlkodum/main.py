from flask import Flask
import random

app = Flask(__name__)

gercekler = ["Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır."
                 "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
                 "Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız.",
                 "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir."]
@app.route("/")
def hello_world():
    return f'<h1>{random.choice(gercekler)}</h1> <a href="/giris">Giriş sayfasına dön</a>'

@app.route("/giris")
def giris():
    return '<h1>Giriş sayfasına hoş geldiniz!</h1>   <a href="/">Rastgele bir gerçeği görüntüle!</a>   <a href="/video">Bağımlılıkla ilgili bir video izle!</a>    <a href="/passwordgenerator">Şifreni oluştur!</a>'

@app.route("/video")
def video():
    return '<iframe width="560" height="315" src="https://www.youtube.com/embed/kS2uFjiN7ns?si=bAOw1r__98z5Nm5y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe> <a href="/giris">Giriş sayfasına dön</a>'

@app.route("/passwordgenerator")
def pgenerator():
    karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    cevap = 8

    sifre = ""

    for i in range(cevap):
        sifre = sifre + random.choice(karakter)
    return f'<h1>{sifre} sizin şifreniz!</h1>  <a href="/giris">Giriş sayfasına dön</a>'

app.run(debug=True)