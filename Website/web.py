from flask import Flask, render_template
import random
import os

app = Flask(__name__)


facts_list = [
"Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
"Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir."
"2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
"2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
"Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.",
"Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
"Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.",
"Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız.",
"x + y = xy değildir birçok kişi bunu maalesef xy sanar fakar xy = x.y demektir x+y ise bilinemez",
"Üçgenin alanını yüksekliğni bilmeden ve sadece kenarlarını bilerk alanını bulabileceğini biliyor muydun! Buna Heron Formülü deniyor ve şu şekilde uygulanıyor: üçgenin kenarlarına x,y ve z diyelim alanını bulmak için x+y+z/2 =  U ise ,U.(u-x).(u-y).(u-z) sayısının kökü üçgenin alanıdır."

]


@app.route("/")
def hello_world():
    return f"<h1>Merhaba!</h1> <h1>Aşağıdaki linklerden istediğini seçebilirsin<h1> <a href='/movies'>Movies</a> <br><br>  <a href='/Y&Z'>Yazı Tura</a> <br><br> <a href='/parola'>Parola oluştur</a> <br><br> <a href='/facts'>Random Facts</a> <br> <br> <a href='/p'>Random Resim</a>"

@app.route('/facts')
def facts():
    return f"<h2>{random.choice(facts_list)}</h2> <a href='/'>Ana sayfa</a>"
    

@app.route("/movies")
def template():
    return render_template("Web.html")

@app.route("/Y&Z")
def yazi_tura():
    a = random.randint(0,2)
    if a == 1:
        b = "Yazı"
    else:
        b = "Tura"
    return f"<h1>{b}</h1> <a href='/'>Ana sayfa</a>"


@app.route("/parola")
def sifre_olusturucu():
    ogeler = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+-/*!&$#?=@<>"
    sifre = ""
    for i in range(20):
        sifre += random.choice(ogeler)       
    return f"<h2>{sifre}</h2> <a href='/'>Ana sayfa</a>"




@app.route('/p')
def resimli_fonksiyon():
    picture = os.path.join(app.static_folder, 'images')
    resim = os.listdir(picture)
    rastgele_image = random.choice(resim)
    return render_template('index.html', image=rastgele_image)

































app.run(debug=True)
