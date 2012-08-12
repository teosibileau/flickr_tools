# -*- coding: latin-1 -*-

from django.core.management.base import BaseCommand, CommandError
from django.contrib.contenttypes.models import ContentType

import flickrapi
from flickrauth.models import *
from datetime import datetime

class Command(BaseCommand):
    args="<slug user_id api_key api_secret>"
    help='Command to create access to flickr api'
    def handle(self,*args,**options):
        if args.__len__()!=4:
            raise CommandError("Wrong number of arguments, 4 needed: %s"%self.args)
        try:
            access=Access.objects.get(slug=args[0])
        except:
            access=Access(slug=args[0])
        access.user=args[1]
        access.key=args[2]
        access.secret=args[3]
        access.save()