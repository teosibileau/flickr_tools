from photosets.models import Account,Photoset, Photo
import flickrapi, datetime, string
from pprint import pprint
from datetime import datetime

# flickr = flickrapi.FlickrAPI('a67f3314d14fbe430ea369870541434b')
# 
# accounts=Account.objects.all()
# 
# for account in accounts:
#     sets = flickr.photosets_getList(user_id=account.user_id,page=1,per_page=2) #change user_id
#     photosets = sets.find('photosets').findall('photoset')
#     #walking photosets
#     for photoset in photosets:
#         print photoset.attrib['id']
#         try:
#             pset=Photoset.objects.get(uid=photoset.attrib['id'])
#             print 'already exits'
#         except:            
#             pset = Photoset()
#             pset.account=account
#             pset.title = photoset[0].text
#             pset.description = photoset[1].text
#             if pset.description is None:
#                 pset.description=''
#             pset.uid = photoset.attrib['id']
#             
#             #save photoset model
#             pset.save()
#         
#         #walking photos
#         for photo in flickr.walk_set(pset.uid):
#             save=False
#             try:
#                 p=Photo.objects.get(uid=photo.attrib['id'])
#                 if p.title != photo.get('title'):
#                     p.title = photo.get('title')
#                     save = True
#             except:
#                 save = True
#                 sizes = flickr.photos_getSizes(photo_id = photo.attrib['id'])
#                 for size in sizes.find('sizes').findall('size'):
#                     if size.attrib['label'] == "Original":
#                         url = size.attrib['source']
#                         break
#                     elif size.attrib['label'] == "Medium":
#                         url = size.attrib['source']
#                 p = Photo(title = photo.get('title'), uid = photo.attrib['id'], photoset = pset, url = url)
#             
#             #save photo model        
#             if save:
#                 p.save()
#                 
# # Recorro cada photoset que aun no haya sido agregado a drupal
# phs = Photoset.objects.filter(added=0)
# for ph in phs:
#     new_node = {'type': 'photoset',
#                 'title': ph.title,
#                 'field_description': { 'und' : { '0' : {'value':ph.description}}},
#                 'field_uid': { 'und' : { '0' : {'value':str(ph.uid)}}},
#                 }
#     node = drupal.call('node.create', new_node)
#     
#     #si se guarda correctamente en drupal entonces se setea added a true    
#     if node != '':
#         pset=Photoset.objects.get(id = ph.id)
#         pset.added = 1
#         pset.save()
# 
# #Recorro cada photo que aun no haya sido agregado a drupal 
# pts = Photo.objects.filter(added=0)
# for pt in pts:
#     new_node = {'type': 'photo',
#                 'title': pt.title,
#                 'field_set_id': { 'und' : { '0' : {'value':pt.id}}},
#                 'field_url': { 'und' : { '0' : {'value':str(pt.url)}}},
#                 }
#     node = drupal.call('node.create', new_node)
#     
#     #si se guarda correctamente en drupal entonces se setea added a true
#     if node != '':
#         p=Photo.objects.get(id = pt.id)
#         p.added = 1
#         p.save()
#     
# 
#  