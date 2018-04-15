from factory import DjangoModelFactory, LazyAttribute, Sequence
from factory.fuzzy import FuzzyText

from tweetable.models import Tweet, User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    name = FuzzyText()
    user_name = FuzzyText()


class TweetFactory(DjangoModelFactory):
    class Meta:
        model = Tweet

    username = Sequence(lambda n: 'person%s' % n)
    context = FuzzyText()
