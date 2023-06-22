
import praw
import sqlite3

#SQLite database'ine bağlandık.
conn = sqlite3.connect('subreddit_posts.db')
c = conn.cursor()

# Table database'de yok ise oluştur bu komutu IF NOT EXIST ile yapıyoruz böylelikle Table'ı 1 kere oluşturuyoruz.
c.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id TEXT PRIMARY KEY,
        title TEXT,
        author TEXT,
        url TEXT
    )
''')


# Kullanıcadan Reddit API bağlantısı için gerekli bilgileri aldık
client_id = input("client ID'inizi giriniz: ")
client_secret = input("client secret'inizi giriniz: ")
user_agent = input("user agent'inizi giriniiz: ")
username = input("Reddit username'inizi giriniz: ")
password = input("Reddit password'unuzu giriniz: ")


#Alınan bilgiler ile Reddit API client'ını başlattık.
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
)


# Subreddit ismini kullanıcıdan aldık.
subreddit_name = input("Postlarına bakmak istediğin subreddit ismini giriniz : ")

# Kaç adet postu çekmek istediğini kullanıcadan alıp değeri çekiyoruz.
subreddit = reddit.subreddit(subreddit_name)
posts = subreddit.new(limit= int(input("Kaç adet çekmek istiyorsunuz(maks:50)")))  

# Postları iterasyon yapıp databasede depoluyoruz
for post in posts:
    post_id = post.id
    title = post.title
    author = post.author.name
    url = post.url

    # post_id'ye göre database olup olmadığına kontro ediyoruz
    c.execute('SELECT * FROM posts WHERE id=?', (post_id,))
    existing_post = c.fetchone()

    if existing_post is None:
        # eğer yoksa database'e insert yapıyoruz
        c.execute('INSERT INTO posts VALUES (?, ?, ?, ?)', (post_id, title, author, url))
        print(f"New post added: {title}")
    else:
        print(f"Post already exists: {title}")

# değişiklikleri database commit ediyoruz
conn.commit()


#tablo çıktısını output olarak görmek istersen.

# c.execute("SELECT * FROM posts")
# rows = c.fetchall()

# # tabloyu yazdırıyoruz
# for row in rows:
#     print(row)


# database bağlantısını kapatıyoruz
conn.close()
