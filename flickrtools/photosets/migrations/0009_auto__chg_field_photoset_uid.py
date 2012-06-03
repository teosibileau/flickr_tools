# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Photoset.uid'
        db.alter_column('photosets_photoset', 'uid', self.gf('django.db.models.fields.BigIntegerField')(unique=True, null=True))


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Photoset.uid'
        raise RuntimeError("Cannot reverse this migration. 'Photoset.uid' and its values cannot be restored.")


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
            'last_checked': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uid': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['photosets']
