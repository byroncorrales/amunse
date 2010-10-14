from urlparse import parse_qs
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@stringfilter
def youthumbnail(value, args):
    '''returns youtube thumb url
    args s, l (small, large)'''
    qs = value.split('?')
    video_id = parse_qs(qs[1])['v'][0]

    if args == 's':
        return "http://img.youtube.com/vi/%s/2.jpg" % video_id
    elif args == 'l':
        return "http://img.youtube.com/vi/%s/0.jpg" % video_id
    else:
        return None

@stringfilter
def youtube_video_id(value):
    qs = value.split('?')
    video_id = parse_qs(qs[1])['v'][0]
    return video_id

register.filter('youthumbnail', youthumbnail)
register.filter('youtube_video_id', youtube_video_id)
