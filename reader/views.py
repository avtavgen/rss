from django.shortcuts import render, get_object_or_404

from reader.models import RssFeed


def get_feed(request):
    news = RssFeed.objects.all()
    return render(request, 'reader/home.html', {"news": news})


def get_description(request, rss_id):
    rss = get_object_or_404(RssFeed, id=rss_id)
    return render(request, 'reader/details.html', {"rss": rss})
