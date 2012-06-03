# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Photoset.added'
        db.delete_column('photosets_photoset', 'added')

        # Deleting field 'Photoset.description'
        db.delete_column('photosets_photoset', 'description')

        # Adding field 'Photoset.last_checked'
        db.add_column('photosets_photoset', 'last_checked', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 6, 2, 21, 5, 8, 298043)), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Photoset.added'
        db.add_column('photosets_photoset', 'added', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Photoset.description'
        raise RuntimeError("Cannot reverse this migration. 'Photoset.description' and its values cannot be restored.")

        # Deleting field 'Photoset.last_checked'
        db.delete_column('photosets_photoset', 'last_checked')


    models = {
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_checked': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uid': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['photosets']
