# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Document'
        db.create_table(u'crm_document_document', (
            (u'entity_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['crm.Entity'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'crm_document', ['Document'])

        # Adding model 'Archive'
        db.create_table(u'crm_document_archive', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm_document.Document'], unique=True)),
            ('keepUntil', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'crm_document', ['Archive'])


    def backwards(self, orm):
        # Deleting model 'Document'
        db.delete_table(u'crm_document_document')

        # Deleting model 'Archive'
        db.delete_table(u'crm_document_archive')


    models = {
        u'crm.entity': {
            'Meta': {'object_name': 'Entity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'links': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'links_rel_+'", 'blank': 'True', 'to': u"orm['crm.Entity']"}),
            'memo': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['crm.Tag']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'crm.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'crm_document.archive': {
            'Meta': {'object_name': 'Archive'},
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm_document.Document']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keepUntil': ('django.db.models.fields.DateField', [], {})
        },
        u'crm_document.document': {
            'Meta': {'object_name': 'Document', '_ormbases': [u'crm.Entity']},
            u'entity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['crm.Entity']", 'unique': 'True', 'primary_key': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['crm_document']