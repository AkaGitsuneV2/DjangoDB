<h1>Список команд</h1>
<h2>Создать двух пользователей (с помощью метода User.objects.create_user('username')).</h2>
from django.contrib.auth.models import User
user1 = User.objects.create_user('user1')
user2 = User.objects.create_user('user2')
<h2>Создать два объекта модели Author, связанные с пользователями</h2>
from News.models import Author
author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)
<h2>Добавить 4 категории в модель Category.</h2>
from News.models import Category
category1 = Category.objects.create(name='Category 1')
category2 = Category.objects.create(name='Category 2')
category3 = Category.objects.create(name='Category 3')
category4 = Category.objects.create(name='Category 4')
<h2>Добавить 2 статьи и 1 новость.</h2>
from News.models import Post
post1 = Post.objects.create(title='Post 1', content='Content 1', author=author1)
post2 = Post.objects.create(title='Post 2', content='Content 2', author=author2)
post3 = Post.objects.create(title='News 1', content='Content 3', post_type='news', author=author1)
<h2>Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).</h2>
post1.categories.add(category1, category2)
post2.categories.add(category3, category4)
post3.categories.add(category1, category3)
<h2>Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий)</h2>
from News.models import CommentCategory, Author
comment1 = CommentCategory.objects.create(post=post1, author=author1, text='Comment 1')
comment2 = CommentCategory.objects.create(post=post2, author=author2, text='Comment 2')
comment3 = CommentCategory.objects.create(post=post3, author=author1, text='Comment 3')
comment4 = CommentCategory.objects.create(post=post1, author=author2, text='Comment 4')
<h2>Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.</h2>
post1.like()
post2.like()
post3.dislike()
comment1.like()
comment2.like()
comment3.dislike()
comment.like()
<h2>Обновить рейтинги пользователей</h2>
from News.models import Author
author1 = Author.objects.get(name='author1')
author1.update_rating()
<h2>Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта)</h2>
