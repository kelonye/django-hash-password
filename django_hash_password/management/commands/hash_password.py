#!/usr/bin/env python

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = 'raw password'
    help = 'Hash password'

    def handle(self, *args, **options):

        raw_password = args[0]

        try:
            from django.contrib.auth.hashers import make_password as fn
        except ImportError:
            from django.contrib.auth.models import get_hexdigest
            import random
            def fn(raw_password):
                algo = 'sha1'
                salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
                hsh = get_hexdigest(algo, salt, raw_password)
                return '%s$%s$%s' % (algo, salt, hsh)

        self.stdout.write('%s\n'%fn(raw_password))
