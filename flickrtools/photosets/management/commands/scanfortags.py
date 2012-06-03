# -*- coding: latin-1 -*-

from django.core.management.base import BaseCommand, CommandError
from django.contrib.contenttypes.models import ContentType

import flickrapi
from flickrtools.flickrauth.models import *
from flickrtools.photosets.models import *

class Command(BaseCommand):
    help='Command to scan new photos tagged with specific instances and asign them to sets'
    def handle(self,*args,**options):
        for access in Access.objects.all():
            # get access for key,secret
            flickr=flickrapi.FlickrAPI(access.key,access.secret)
            (token, frob) = flickr.get_token_part_one(perms='write')
            if not token: raw_input("Press ENTER after you authorized this program")
            flickr.get_token_part_two((token, frob))
            for uset in Photoset.objects.filter(access=access):
                # get photos with given tags
                if uset.last_checked:
                    photos=flickr.walk(user_id=access.user,tags=uset.tags,tag_mode='AND',min_taken_time=uset.last_checked)
                else:
                    photos=flickr.walk(user_id=access.user,tags=uset.tags,tag_mode='AND')
                photos=[photo for photo in photos]
                if not uset.uid:
                    uset.uid=flickr.photosets_create(title=uset.title,primary_photo_id=photos[0].get('id'))[0].get('id')
                for photo in photos:
                    flickr.photos_setPerms(photo_id=photo.get('id'),is_public=1,is_friend=0,is_family=0,perm_comment=3,perm_addmeta=0)
                    try:
                        flickr.photosets_addPhoto(photoset_id=uset.uid,photo_id=photo.get('id'))
                    except:
                        pass
                uset.save()