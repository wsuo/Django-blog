from django.shortcuts import render
from django.core.paginator import Paginator as pG

# Create your views here.
from article.models import Article


def index(req):
    articles = Article.objects.all()
    p = req.GET.get('page')
    p = int(p) if p else 1
    pl = pG(articles, 3)
    pn = pl.num_pages  # 总页数
    pal = pl.page(p)  # 每一页中的集合
    if pal.has_next():
        np = p + 1
    else:
        np = p
    if pal.has_previous():
        pp = p - 1
    else:
        pp = p
    return render(req, 'index.html',
                  {'articles': pal,
                   'cur_page': p,
                   'prev_page': pp,
                   'next_page': np,
                   'num': range(1, pn + 1)}
                  )


def get_detail_page(req, article_id):
    all_article = Article.objects.all()
    curr_article = None
    prev_idx = 0
    next_idx = 0
    prev_article = None
    next_article = None
    for idx, article in enumerate(all_article):
        if idx == 0:
            prev_idx = 0
            next_idx = idx + 1
        elif idx == len(all_article) - 1:
            prev_idx = idx - 1
        else:
            prev_idx = idx - 1
            next_idx = idx + 1
        if article.article_id == article_id:
            curr_article = article
            prev_article = all_article[prev_idx]
            next_article = all_article[next_idx]
            break
    return render(req, 'detail.html', {
        'curr_article': curr_article,
        'prev_article': prev_article,
        'next_article': next_article
    })
