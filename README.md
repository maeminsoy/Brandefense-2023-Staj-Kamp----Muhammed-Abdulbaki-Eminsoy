# Brandefense 2023 Staj Kampı | Muhammed Abdülbaki Eminsoy
 Fetching post from subreddits and store them in database 

Öncelikle Reddit'in API client serverı iletişime geçmek için clint id, client secret, user agent, username ve password bilgilerini elde etmemiz lazım. 
https://www.reddit.com/prefs/apps/ Bu linkten client id, client secret ve user agent bilgilerini elde edicez.

Linke tıkladıktan sonra create application kısmında scripti seçiyoruz daha sonra name, description ve redirect uri kısımlarını dolduruyoruz. 
![image](https://github.com/maeminsoy/Brandefense-2023-Staj-Kamp----Muhammed-Abdulbaki-Eminsoy/assets/137301030/ea7666c5-dd79-48a4-9f2c-e5d3c6dd3c65)

Bu işlemleri tamamladıktan sonra create app seçeneğine basıp aşağıdaki resimdeki kısma geliyoruz buradan kullanıcı ile ilgili ihtiyacımız olan bilgileri elde ediyoruz. 
![image](https://github.com/maeminsoy/Brandefense-2023-Staj-Kamp----Muhammed-Abdulbaki-Eminsoy/assets/137301030/c59d4bda-3e25-43cb-a0dc-02aa92123a9a)

Resimdeki bilgiler doğrultusunda 

client id'miz : YSWQn9Qp_Q2Z0zK5rRSv3w 

client secret'ımız: ixLJdxN-qqCePbDdr3AsI_VHYkZsEw 

Reddit uygulaması user agent'ı <platform>:<app ID>:<version string> (by /u/<Reddit username>) bu formatta istiyor. Burdaki platform, app, version değerlerini kendimiz atayabiliyoruz. Ben bu şekilde bir atama yaptım.
user agent'ımız: python:fetchposts:1.0 (by /u/Ok-Championship-7621)

username'imiz: Ok-Championship-7621

Bu bilgileri elde ettikten sonra kodumuzu çalıştırabiliriz...
