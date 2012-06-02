# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Photo.created'
        db.delete_column('photosets_photo', 'created')

        # Deleting field 'Photoset.created'
        db.delete_column('photosets_photoset', 'created')


    def backwards(self, orm):
        
        # Adding field 'Photo.created'
        db.add_column('photosets_photo', 'created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 2, 10, 13, 43, 31, 629461)), keep_default=False)

        # Adding field 'Photoset.created'
        db.add_column('photosets_photoset', 'created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 2, 10, 13, 43, 44, 13605)), keep_default=False)


    models = {
        'photosets.account': {
            'Meta': {'object_name': 'Account'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'photosets.photo': {
            'Meta': {'object_name': 'Photo'},
            'added': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photoset': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photos'", 'to': "orm['photosets.Photoset']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'uid': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'photosets.photoset': {
            'Meta': {'object_name': 'Photoset'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photosets'", 'to': "orm['photosets.Account']"}),
            'added': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1700'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uid': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['photosets']
