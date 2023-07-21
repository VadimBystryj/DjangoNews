from News_Portal.models import *

u1 = User.objects.create_user(username ='Vadzim')
u2 = User.objects.create_user(username = 'Victorya')

Author.objects.create(authorUser = u1)
Author.objects.create(authorUser = u2)
Category.objects.create(name = 'IT')
Category.objects.create(name = 'Politicts')
Category.objects.create(name = 'Culture')
Category.objects.create(name = 'Science')
Category.objects.create(name = 'Sport')
author = Author.objects.get(id=3)
Post.objects.create(author = author, categoryType = 'AR', title = 'python разработчик', text = 'Записывайтесь в школу Skillfactory и становитесь разрабочиками на Python')
author = Author.objects.get(id=4)
Post.objects.create(author = author, categoryType = 'NW', title = 'Марафон', text = 'В Гданьске пройдет очередной марафон')
author = Author.objects.get(id=4)
Post.objects.create(author = author, categoryType = 'AR', title = 'Методы запоминания', text = 'Существует несколько методов эффективного запоминания информации')
Post.objects.get(id = 2).category.add(Category.objects.get(id=5), Category.objects.get(id=8))
Post.objects.get(id = 4).category.add(Category.objects.get(id=7), Category.objects.get(id=9))
Post.objects.get(id = 5).category.add(Category.objects.get(id = 8))
Comment.objects.create(commentPost = Post.objects.get(id=2), commentUser=Author.objects.get(id=3).authorUser, text='Дайте пожалуйста номер для связи')
Comment.objects.create(commentPost = Post.objects.get(id=4), commentUser=Author.objects.get(id=4).authorUser, text='Где можно записаться?')
Comment.objects.create(commentPost = Post.objects.get(id=5), commentUser=Author.objects.get(id=3).authorUser, text='Где купить такую книгу?')
Comment.objects.create(commentPost = Post.objects.get(id=4), commentUser=Author.objects.get(id=4).authorUser, text='Какие условия для бега в этом Городе?')
Comment.objects.get(id=2).like()
Comment.objects.get(id=2).dislike()
Comment.objects.get(id=2).dislike()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=4).dislike()
Comment.objects.get(id=5).dislike()
a = Author.objects.get(id=3)
a.update_rating()
Post.objects.get(id=2).like()
Post.objects.get(id=2).like()
Post.objects.get(id=2).like()
Post.objects.get(id=2).like()
Post.objects.get(id=2).dislike()
a = Author.objects.order_by('-ratingAuthor')[:1]
a
a.ratingAuthor
for i in a:
    i.ratingAuthor
    i.authorUser.commentUser
a = Post.objects.order_by('-rating')[:1]
a
for i in a:
    i.dateCreation
    i.rating
    i.title
    i.preview()
Post.objects.order_by('-rating')[0].comment_set.all().values('dateCreation', 'commentUser__username', 'rating', 'text')