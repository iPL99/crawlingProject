from django.db import models

class News(models.Model):
    articleCd = models.IntegerField(primary_key=True)
    news_organization_name = models.TextField()
    ranking_date = models.DateField()
    ranking = models.IntegerField()
    article_title = models.TextField()
    reporter_name = models.TextField()
    article_section = models.TextField()
    monthly_article_count = models.IntegerField()

    class Meta:
        db_table = 'article'  # 이 모델은 'article' 테이블과 연동됩니다.
