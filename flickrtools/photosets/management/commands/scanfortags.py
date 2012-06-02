# -*- coding: latin-1 -*-

from django.core.management.base import BaseCommand, CommandError
from django.contrib.contenttypes.models import ContentType

from flickrtools.photosets.models import *

class Command(BaseCommand):
    help='Command to scan new photos tagged with specific instances and asign them to sets'
    def handle(self,*args,**options):
        pass