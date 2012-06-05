from celery.task import task
from django.core import serializers
import flickrapi
import string
import sys

@task
def addPhoto(access,uset,photo):
    flickr=flickrapi.FlickrAPI(access.key,access.secret)
    (token, frob) = flickr.get_token_part_one(perms='write')
    if not token: raw_input("Press ENTER after you authorized this program")
    flickr.get_token_part_two((token, frob))
    if not flickr.photos_getPerms(photo_id=photo.get('id'))[0].get('ispublic'):
        flickr.photos_setPerms(photo_id=photo.get('id'),is_public=1,is_friend=0,is_family=0,perm_comment=3,perm_addmeta=0)
    try:
        response=flickr.photosets_addPhoto(photoset_id=uset.uid,photo_id=photo.get('id'))
    except flickrapi.exceptions.FlickrError as error:
        response=error
    return response