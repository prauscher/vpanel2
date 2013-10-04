# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Split.account'
        db.delete_column(u'accounting_split', 'account_id')

        # Adding M2M table for field accounts on 'Split'
        m2m_table_name = db.shorten_name(u'accounting_split_accounts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('split', models.ForeignKey(orm[u'accounting.split'], null=False)),
            ('account', models.ForeignKey(orm[u'accounting.account'], null=False))
        ))
        db.create_unique(m2m_table_name, ['split_id', 'account_id'])


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Split.account'
        raise RuntimeError("Cannot reverse this migration. 'Split.account' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Split.account'
        db.add_column(u'accounting_split', 'account',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounting.Account']),
                      keep_default=False)

        # Removing M2M table for field accounts on 'Split'
        db.delete_table(db.shorten_name(u'accounting_split_accounts'))


    models = {
        u'accounting.account': {
            'Meta': {'object_name': 'Account'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounting.Account']", 'null': 'True', 'blank': 'True'})
        },
        u'accounting.journal': {
            'Meta': {'object_name': 'Journal'},
            'allowNull': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'rootAccounts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['accounting.Account']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'accounting.record': {
            'Meta': {'object_name': 'Record'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'accounting.split': {
            'Meta': {'object_name': 'Split'},
            'accounts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['accounting.Account']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounting.Record']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['accounting']