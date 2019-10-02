from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.feedgenerator import Atom1Feed
from spirit.comment.models import Comment
from spirit.topic.models import Topic
from spirit.user.models import UserProfile

class ActiveTopicsFeed(Feed):
    feed_type = Atom1Feed
    title = 'Trifulca - Activos'
    link = '/'
    description = 'Temas del foro ordenados por actividad'
    description_template = 'feeds/topic.html'

    def items(self):
        return Topic.objects\
            .visible()\
            .global_()\
            .order_by('-last_active')\
            .select_related('category')[:10]

    def item_title(self, topic):
        return topic.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic = context['obj']

        comments = Comment.objects\
            .for_topic(topic=topic)\
            .order_by('date')

        context['topic'] = topic
        context['comments'] = comments
        context['users'] = get_usernames()

        return context

    def item_pubdate(self, item):
        return item.last_active

    def item_link(self, item):
        return reverse('spirit:topic:detail', args=[item.pk, item.slug])


def get_usernames():
    return [profile.user.username for profile in UserProfile.objects.all()]

