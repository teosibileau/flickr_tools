from celery.task import task

import flickrapi

@task
def addPhoto(access,uset,photo):
    print "adding %s in set %s for %s access"%(photo.get('id'),uset.uid,access.user)
    flickr=flickrapi.FlickrAPI(access.key,access.secret)
    flickr.photos_setPerms(photo_id=photo.get('id'),is_public=1,is_friend=0,is_family=0,perm_comment=3,perm_addmeta=0)
    try:
        response=flickr.photosets_addPhoto(photoset_id=uset.uid,photo_id=photo.get('id'))
    except:
        response='Something went grong'
    return response