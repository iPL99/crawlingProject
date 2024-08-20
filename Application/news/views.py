# render 함수는 클라이언트의 요청을 처리하여 최종 결과인 HTML 문서를 클라이언트에게
# 되돌려 주는 역할을 합니다.
from django.shortcuts import render
from news.models import News  # 절대 경로 임포트
from django.db.models import Count
import json
# Create your views here.
def main_page(request): # 메인 페이지 호출하기
    return render(request, 'kmdb/main.html')
# end def

def news_list(request):
    news_list = News.objects.all()  # 모든 뉴스 항목을 가져옵니다.
    return render(request, 'kmdb/news_list.html', {'newsList': news_list})


from django.shortcuts import render
from news.models import News
from django.db.models import Count
import json


def reporter_comparison(request):
    # 날짜 범위 설정
    start_date = '2024-07-13'
    end_date = '2024-08-13'

    # 각 언론사에서 가장 많은 기사를 쓴 상위 3명의 기자를 저장할 딕셔너리
    top_reporters = {'서울신문': [], '세계일보': []}

    for org in top_reporters.keys():
        # 해당 언론사와 날짜 범위에 따른 기자별 기사 수 집계
        results = News.objects.filter(
            news_organization_name=org,
            ranking_date__range=[start_date, end_date]
        ).values('reporter_name').annotate(article_count=Count('reporter_name')).order_by('-article_count')[:3]

        # 상위 3명의 기자 추출 및 딕셔너리로 변환
        top_reporters[org] = list(results)

    # 데이터를 JSON으로 직렬화
    context = {
        'top_reporters': json.dumps(top_reporters),
    }
    return render(request, 'kmdb/reporter_comparison.html', context)
