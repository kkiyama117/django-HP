from django.core.management.base import BaseCommand

import transfacils.initializer


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
        transfacils.initializer.initialize()
