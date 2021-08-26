from django.core.management.base import BaseCommand, CommandError
from home.models import Article
from home.utils import check_code


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        articles = Article.objects.all()
        old_codes = articles.count()
        new_codes = 0
        for article in articles:
            article.shortcode = check_code(article)
            article.save()
            new_codes += 1

            print(article.shortcode)
        return f'Success generate {new_codes} from {old_codes} codes'
