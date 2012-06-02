# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Account'
        db.delete_table('photosets_account')

        # Adding model 'Access'
        db.create_table('photosets_access', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('secret', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('photosets', ['Access'])

        # Deleting field 'Photoset.account'
        db.delete_column('photosets_photoset', 'account_id')


    def backwards(self, orm):
        # Adding model 'Account'
        db.create_table('photosets_account', (
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('photosets', ['Account'])

        # Deleting model 'Access'
        db.delete_table('photosets_access')


        # User chose to not deal with backwards NULL issues for 'Photoset.account'
        raise RuntimeError("Cannot reverse this migration. 'Photoset.account' and its values cannot be restored.")

    models = {
        'photosets.access': {
            'Meta': {'object_name': 'Access'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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
            'added': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1700'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uid': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['photosets']