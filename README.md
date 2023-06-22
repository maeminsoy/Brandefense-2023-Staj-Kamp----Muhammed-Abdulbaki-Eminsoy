# Brandefense 2023 Staj Kampı | Muhammed Abdülbaki Eminsoy
 Fetching post from subreddits and store them in database 

Öncelikle Reddit'in API client serverı iletişime geçmek için clint id, client secret, user agent, username ve password bilgilerini elde etmemiz lazım. 
https://www.reddit.com/prefs/apps/ Bu linkten client id, client secret ve user agent bilgilerini elde edicez.

Linke tıkladıktan sonra create application kısmında scripti seçiyoruz daha sonra name, description ve redirect uri kısımlarını dolduruyoruz. 
![image](https://github.com/maeminsoy/Brandefense-2023-Staj-Kamp----Muhammed-Abdulbaki-Eminsoy/assets/137301030/ea7666c5-dd79-48a4-9f2c-e5d3c6dd3c65)

Bu işlemleri tamamladıktan sonra create app seçeneğine basıp aşağıdaki resimdeki kısma geliyoruz buradan kullanıcı ile ilgili ihtiyacımız olan bilgileri elde ediyoruz. 
![image](https://github.com/maeminsoy/Brandefense-2023-Staj-Kamp----Muhammed-Abdulbaki-Eminsoy/assets/137301030/fb3a5b3e-e7b2-4cd3-a709-e0a3e704d77c)


Resimdeki bilgiler doğrultusunda 

Reddit uygulaması user agent'ı <platform>:<app ID>:<version string> (by /u/<Reddit username>) bu formatta istiyor. Burdaki platform, app, version değerlerini kendimiz atayabiliyoruz. Ben bu şekilde bir atama yaptım.
user agent'ımız: python:fetchposts:1.0 (by /u/Ok-Championship-7621)

Bu bilgileri elde ettikten sonra kodumuzu çalıştırabiliriz.

Dockerize edilmesi 
"docker -t build image_name ." bu komut ile docker image'imizi oluştururuz.
"docker run image_name" bu komut ile de docker image'imizi çalıştırırız.

BUNLARI YAPMADAN ÖNCE docker.py FİLE İÇERİSİNDEKİ BİLGİLELRİNİZİ GÜNCELLEYİN.
