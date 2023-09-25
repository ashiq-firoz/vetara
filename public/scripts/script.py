import sys
tag = sys.argv[1]

d = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}


ans = []
if tag=='govrt':
    print(30)
    print(20)
    print(50)
else:
    print(30)
    print(20)
    print(50)
print(ans)

sys.stdout.flush()

# from transformers import pipeline

# pipe  = pipeline(task = 'sentiment-analysis",model = 'shashanksrinath/News_Sentiment_Analysis')


# tag = sys.argv[1]

# data = ""

# import newspaper

# urls = [
#     "https://www.mathrubhumi.com/latest-news",
# ]

# langs = ["te","kn","ta","ml"]

# tags = [
#     "bill",
# ]

# url_list = set()

# for url in urls:
#     print("======================================================================================")
#     url += tag
#     print("url ::",url)
#     urls_set = set()
#     print("collecting links....")
#     cnn_articles = newspaper.build(url, memoize_articles=False)
#     for article in cnn_articles.articles:
#         # check to see if the article url is not within the urls_set
#         if article.url not in urls_set:
#             # add the unique article url to the set
#             urls_set.add(article.url)
#             #articles.append(article.url)
#     # print("filtering...")
#     # s = set()
#     # for link in urls_set:
#     #     for tag in tags:
#     #         if tag in link:
#     #             print(link,end=" ")
#     #             s.add(link)
#     #             break
#     # print(end="/n")
#     url_list.update(urls_set)


# from translate import Translator


# print("Extracting data")
# for link in url_list:
#     translator= Translator(from_lang="ml",to_lang="en")
#     print("url::",link)
#     if tags[0] not in link:
#       continue
#     article = newspaper.Article(url=link, language='en')
#     article.download()
#     article.parse()
#     article ={
#     "title": str(article.title),
#     "text": str(article.text),
#     "authors": article.authors,
#     "published_date": str(article.publish_date),
#     "top_image": str(article.top_image),
#     "videos": article.movies,
#     "keywords": article.keywords,
#     "summary": str(article.summary)
#     }
#     l = article['text'].split(".")
#     for i in l:
#       data += translator.translate(i)

# res = pipe(data, return_all_scores=True)
# ans = []
# for i in res[0]:
#   ans.append(i['score'])
# print(ans) #[neg,neut,pos]
