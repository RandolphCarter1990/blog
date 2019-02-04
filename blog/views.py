from django.shortcuts import render, get_object_or_404
from .models import Article,Category
from django.views import View

class BaseView(View):

    latest_articles_list = Article.objects.order_by('-pub_date')[:2]


    context = {
        'latest_articles_list': latest_articles_list,
    }

    top_categories = Category.objects.order_by('-popularity')[:3]

    context['popular_categories'] = Category.objects.order_by('-popularity')[:3]
    
    top_articles = {}
    for category in top_categories:
        top_article = category.article_set.all()[:1].get()
        top_articles[category.title] = top_article

    context['top_articles'] = top_articles    

    def get(self,request):
        
        articles_categorys_list = list()
        return render (request, 'blog/index.html', self.context)

class ArticlePage(BaseView):

    def get(self,request,article_id):
        article = get_object_or_404(Article, id=article_id)
        article.visits += 1
        article.save()
        categories = article.category.all()
        for category in categories:
            category.popularity += 1
            category.save()
        
        self.context['article'] = article

        
        
        return render (request, 'blog/article-page.html', self.context)


