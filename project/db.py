import psycopg2
class DB(object):
 def __init__(self):
     self.conn = psycopg2.connect(host='127.0.0.1', database='tfa',
     user='postgres', password='suprita11')
     self.cursor = self.conn.cursor()
 #getsources
 def get_sources(self):
     query = "select url, category from sources"
     self.cursor.execute(query)
     return self.cursor.fetchall()
     print(self.cursor.fetchall())
 def insert_news(self, newsitems, category):
     for item in newsitems:
         try:
             query = "insert into news(title, description, post_link, " \
             "category) " \
             "values(%s, %s, %s, %s)"
             self.cursor.execute(query, (item['title'], item['description'],
             item['link'], category))
             self.conn.commit()
         except Exception as e:
             print(str(e))
 def read_news_limit(self):
     query = "select title from news where category='top'"
     self.cursor.execute(query)
     return self.cursor.fetchall()
 def filter(self,category,limit):
     #query="select * from news order by id desc limit {}".format(limit)
     query="select * from news where category=%s order by id desc  limit %s "
     self.cursor.execute(query,(category,limit))
     return self.cursor.fetchall()
 def insert_sources(self,url,category):
     try:
         #query="insert into sources(url, category)values('https://timesofindia.indiatimes.com/rssfeedstopstories.cms', 'mat')"
         query="insert into sources(url,category)values(%s,%s)"
         self.cursor.execute(query,(url,category))
         self.conn.commit()
     except Exception as e:
          print(str(e))      
                    
 #read news items
 #filter news items
 #insert news item
if __name__ == '__main__':
    m=int(input("enter your option 1.top stories 2.filter by category 3.aggregate 4.delete"))
    if m==1:
        d1=DB()
        print(d1.get_sources())
        y=d1.read_news_limit()
        for item in y:
            print(item[0])
    if m==2:
        d1=DB()
        m=input("enter a category")
        n=int(input("enter a limit"))
        print(d1.filter(m,n))
        #k=d1.filter(m,n)
        #for item in k:
           # print(item[1])

    if m==3:
        d1=DB()
        m=input("enter the url")
        n=input("enter the category")
        print(d1.insert_sources(m,n))                    
                             
    
    else:
        print("chosse correct option")

        
