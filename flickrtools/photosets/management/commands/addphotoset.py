# -*- coding: latin-1 -*-

from django.core.management.base import BaseCommand, CommandError
from django.contrib.contenttypes.models import ContentType

import flickrapi
from flickrauth.models import *
from photosets.models import *
from datetime import datetime

class Command(BaseCommand):
    args="<access_slug photoset_title photoset_tags>"
    help='Command to add watched photoset'
    def handle(self,*args,**options):
        if args.__len__()!=3:
            raise CommandError("Wrong number of arguments, 3 needed: %s"%self.args)
        try:
            access=Access.objects.get(slug=args[0])
        except:
            raise CommandError("Access does not yet exits, please create with python manage.py addaccess <args>")
        try:
            photoset=Photoset.objects.get(title=args[1],access=access)
        except:
            photoset=Photoset(title=args[1],access=access)
        photoset.tags=args[2]
        photoset.save()
