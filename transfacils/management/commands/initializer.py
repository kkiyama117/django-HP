from django.core.management.base import BaseCommand

import transfacils.helpers.initializer
from transfacils import helpers


class Command(BaseCommand):
    help = 'Initialize stations'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        # parser.add_argument('route_cd', nargs='+', type=int)

        # # Named (optional) arguments
        # parser.add_argument(
        #     '--delete',
        #     action='store_true',
        #     dest='delete',
        #     help='Delete data ',
        # )

    def handle(self, *args, **options):
        helpers.initializer.initialize_lines_db()
