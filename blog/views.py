from django.shortcuts import render
from django.utils import timezone
from .models import Post, Category, Comment
from bs4 import BeautifulSoup


def home(request):
    return category(request, '')


def article(request, year, month, day, title):
    post_qs = Post.objects.filter(published_date__lte=timezone.now()).order_by(
                                  '-published_date')
    posts = []
    c = []
    for post in post_qs:
        category_qs = Category.objects.filter(post_id=post.id)
        category_of_post = [q.category for q in category_qs]
        c += category_of_post
        posts.append((post, category_of_post))

    post_qs = Post.objects.filter(published_date__year=year,
                                  published_date__month=month,
                                  published_date__day=day,
                                  title=title)
    posts_filter = []
    if post_qs.count():
        post = post_qs[0]
        category_qs = Category.objects.filter(post_id=post.id)
        category_of_post = [q.category for q in category_qs]

        if request.method == 'POST':
            name = request.POST['name']
            print(name)
            text = request.POST['text']
            post.comment_set.create(name=name, text=text)

        comment_qs = Comment.objects.filter(post_id=post.id).order_by(
                                            '-date')
        posts_filter.append((post, category_of_post, comment_qs.count()))

    c = list(set(c))
    c2 = []
    for c1 in c:
        c2.append((c1, Category.objects.filter(category=c1).count()))
    return render(request, 'blog/article.html',
                  {'posts_filter': posts_filter,
                   'posts': posts[0:10],
                   'comments': comment_qs,
                   'posts_count_all': Post.objects.all().count(),
                   'c2': c2})


def category(request, category):
    # filter results
    post_qs = Post.objects.filter(published_date__lte=timezone.now()).order_by(
                                '-published_date')
    # list of tuple (post, category)
    posts = []
    c = []
    for post in post_qs:
        category_qs = Category.objects.filter(post_id=post.id)
        category_of_post = [q.category for q in category_qs]
        c += category_of_post
        post.text = BeautifulSoup(post.text).get_text()[0:300]
        comment_qs = Comment.objects.filter(post_id=post.id)
        posts.append((post, category_of_post, comment_qs.count()))

    if(len(category)):
        q = Category.objects.filter(category=category)
        post_qs = Post.objects.filter(category=q)
        posts_filter = []
        for post in post_qs:
            category_qs = Category.objects.filter(post_id=post.id)
            category_of_post = [q.category for q in category_qs]
            post.text = BeautifulSoup(post.text).get_text()[0:300]
            comment_qs = Comment.objects.filter(post_id=post.id)
            posts_filter.append((post, category_of_post, comment_qs.count()))
    else:
        posts_filter = posts

    c = list(set(c))
    c2 = []
    for c1 in c:
        c2.append((c1, Category.objects.filter(category=c1).count()))
    return render(request, 'blog/post_list.html',
                  {'posts': posts[0:10],
                   'posts_count': len(posts),
                   'posts_filter': posts_filter,
                   'posts_filter_count': len(posts_filter),
                   'posts_count_all': Post.objects.all().count(),
                   'c2': c2})
