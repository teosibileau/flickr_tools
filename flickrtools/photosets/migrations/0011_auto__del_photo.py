# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Photo'
        db.delete_table('photosets_photo')


    def backwards(self, orm):
        
        # Adding model 'Photo'
        db.create_table('photosets_photo', (
            ('uid', self.gf('django.db.models.fields.BigIntegerField')(unique=True)),
            ('published_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('photoset', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photos', to=orm['photosets.Photoset'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('added', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('photosets', ['Photo'])


    models = {
        'flickrauth.access': {
            'Meta': {'object_name': 'Access'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
