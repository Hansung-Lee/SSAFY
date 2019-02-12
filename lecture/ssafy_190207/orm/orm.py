# articles (게시물)
# id, title, content, author

# list / tuple
articles_list = [
    (1, '제목1', '내용1', '글쓴이1'),
    (2, '제목2', '내용2', '글쓴이2')
]
    
# dict
articles_dict = [
    {'id': 1, 'title': '제목1', 'content': '내용1', 'author': '글쓴이1'},
    {'id': 2, 'title': '제목2', 'content': '내용2', 'author': '글쓴이2'}
]

# object
class Articles:
    def __init__(self, id, title, content, author):
        self.id = id
        self.title = title
        self.content = content
        self.author = author
    
    def update(self, id, title, content, author):
        self.id = id
        self.title = title
        self.content = content
        self.author = author
        
    def __str__(self):
        return "이 글은 {}가 쓴 글입니다.".format(self.author)
    
articles_object = [
    Articles(1, '제목1', '내용1', '글쓴이1'),
    Articles(2, '제목2', '내용2', '글쓴이2')
]

print(articles_list[1][3])
print(articles_dict[1].get('author'))
print(articles_object[1].author)

# object update()
two = articles_object[1]
two.update(3, '제목3', '내용3', '글쓴이3')
print(articles_object[1].author)

# object str()
two = articles_object[1]
print(str(two))