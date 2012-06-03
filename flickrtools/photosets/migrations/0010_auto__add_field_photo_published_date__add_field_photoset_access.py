# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Photo.published_date'
        db.add_column('photosets_photo', 'published_date', self.gf('django.db.models.fields.DateTimeField')(default=1), keep_default=False)

        # Adding field 'Photoset.access'
        db.add_column('photosets_photoset', 'access', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='photosets', to=orm['flickrauth.Access']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Photo.published_date'
        db.delete_column('photosets_photo', 'published_date')

        # Deleting field 'Photoset.access'
        db.delete_column('photosets_photoset', 'access_id')


    models = {
        'flickrauth.access': {
            'Meta': {'object_name': 'Access'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'photosets.photo': {
            'Meta': {'object_name': 'Photo'},
            'added': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photoset': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photos'", 'to': "orm['photosets.Photoset']"}),
            'published_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'uid': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'photosets.photoset': {
            'Meta': {'object_name': 'Photoset'},
            'access': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photosets'", 'to': "orm['flickrauth.Access']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_checked': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uid': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['photosets']
