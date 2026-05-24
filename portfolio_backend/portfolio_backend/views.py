from django.http import HttpResponse, HttpResponseNotFound
from pathlib import Path
from django.conf import settings


def index(request):
    # The HTML file lives at the project root (one level above BASE_DIR)
    html_path = Path(settings.BASE_DIR).parent / 'ernest_anyona_portfolio.html'
    try:
        content = html_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return HttpResponseNotFound('<h1>Portfolio page not found</h1>')
    return HttpResponse(content, content_type='text/html')
