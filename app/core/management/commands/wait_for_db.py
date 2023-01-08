"""
Django command to wait for db to be available.
"""
import time

""" this is the error as thrown from the psychology to package sometimes when the database isn't ready"""
from psycopg2 import OperationalError as Psycopg2OpError

"""This is the error django throws when db isn't ready"""
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("waiting for database....")
        db_up=False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up=True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))