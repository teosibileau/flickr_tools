# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Account'
        db.create_table('photosets_account', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('photosets', ['Account'])

        # Adding model 'Photoset'
        db.create_table('photosets_photoset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photosets', to=orm['photosets.Account'])),
            ('uid', self.gf('django.db.models.fields.BigIntegerField')(unique=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1700)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('photosets', ['Photoset'])

        # Adding model 'Photo'
        db.create_table('photosets_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photoset', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photos', to=orm['photosets.Photoset'])),
            ('uid', self.gf('django.db.models.fields.BigIntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('photosets', ['Photo'])

    def backwards(self, orm):
        
        # Deleting model 'Account'
        db.delete_table('photosets_account')

        # Deleting model 'Photoset'
        db.delete_table('photosets_photoset')

        # Deleting model 'Photo'
        db.delete_table('photosets_photo')

    models = {
        'photosets.account': {
            'Meta': {'object_name': 'Account'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'photosets.photo': {
            'Meta': {'object_name': 'Photo'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photoset': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photos'", 'to': "orm['photosets.Photoset']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'uid': ('django.db.models.fields.BigIntegerField', [], {}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'photosets.photoset': {
            'Meta': {'object_name': 'Photoset'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photosets'", 'to': "orm['photosets.Account']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1700'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uid': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['photosets']
