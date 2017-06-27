import os
import shlex
import time

from subprocess import Popen

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from deals.models import Company


class Command(BaseCommand):
    help = 'Runs the spider for the specified company'

    def add_arguments(self, parser):
        parser.add_argument('company_name', nargs='+', type=str)

    def handle(self, *args, **options):
        os.chdir(os.path.join(settings.BASE_DIR, 'scraper', 'scraper'))
        running_procs = []

        for company_name in options['company_name']:
            try:
                company = Company.objects.get(name__iexact=company_name)
            except Company.DoesNotExist:
                raise CommandError('Company "%s" does not exist' % company_name)

            command_line = settings.SCRAPY_CMD + ' crawl ' + company.spider_name
            args = shlex.split(command_line)
            running_procs.append(Popen(args))

        while running_procs:
            for proc in running_procs:
                retcode = proc.poll()
                if retcode is not None:  # Process finished.
                    running_procs.remove(proc)
                    break
                else:  # No process is done, wait a bit and check again.
                    time.sleep(10)
                    continue
