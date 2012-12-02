# -*- coding: latin-1 -*-

from django.core.management.base import BaseCommand, CommandError
from django.contrib.contenttypes.models import ContentType

import flickrapi
from flickrauth.models import *
from photosets.models import *
from photosets.tasks import addPhoto
from datetime import datetime

class Command(BaseCommand):
    help='Command to scan new photos tagged with specific instances and asign them to sets'
    def handle(self,*args,**options):
        for access in Access.objects.all():
            # get access for key,secret
            flickr=flickrapi.FlickrAPI(access.key,access.secret)
            (token, frob) = flickr.get_token_part_one(perms='write')
            if not token: raw_input("Press ENTER after you authorized this program")
            flickr.get_token_part_two((token, frob))
            # for photoset defined for this access
            for uset in access.photosets.all():
                # get photos with given tags
                if uset.last_checked:
                    self.stdout.write('last cheched %s\n'%uset.last_checked)
                    # if last_checked instance use it to narrow picture search
                    photos=flickr.walk(user_id=access.user,tags=uset.tags,tag_mode='AND',min_upload_date=uset.last_checked)
                else:
                    # if not bring them all
                    photos=flickr.walk(user_id=access.user,tags=uset.tags,tag_mode='AND')
                photos=[photo for photo in photos]
                self.stdout.write('%s new photos to add\n'%photos.__len__())
                if not uset.uid:
                    av_photosets=flickr.photosets_getList()[0]
                    av_photosets_titles=[photoset[0].text for photoset in av_photosets]
                    if not uset.title in av_photosets_titles:
                        uset.uid=flickr.photosets_create(title=uset.title, primary_photo_id=photos[0].get('id'))[0].get('id')
                    else:
                        uset.uid=av_photosets[av_photosets_titles.index(uset.title)].get('id')
                for photo in photos:
                    addPhoto.delay(access,uset,photo)
                # Save Timestamp to photoset instance
                uset.last_checked=datetime.now()
                uset.save()