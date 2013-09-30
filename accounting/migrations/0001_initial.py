# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Journal'
        db.create_table(u'accounting_journal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('allowNull', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'accounting', ['Journal'])

        # Adding M2M table for field rootAccounts on 'Journal'
        m2m_table_name = db.shorten_name(u'accounting_journal_rootAccounts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('journal', models.ForeignKey(orm[u'accounting.journal'], null=False)),
            ('account', models.ForeignKey(orm[u'accounting.account'], null=False))
        ))
        db.create_unique(m2m_table_name, ['journal_id', 'account_id'])

        # Adding model 'Account'
        db.create_table(u'accounting_account', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounting.Account'], null=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'accounting', ['Account'])

        # Adding model 'Record'
        db.create_table(u'accounting_record', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'accounting', ['Record'])

        # Adding model 'Split'
        db.create_table(u'accounting_split', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounting.Record'])),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounting.Account'])),
            ('note', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'accounting', ['Split'])


    def backwards(self, orm):
        # Deleting model 'Journal'
        db.delete_table(u'accounting_journal')

        # Removing M2M table for field rootAccounts on 'Journal'
        db.delete_table(db.shorten_name(u'accounting_journal_rootAccounts'))

        # Deleting model 'Account'
        db.delete_table(u'accounting_account')

        # Deleting model 'Record'
        db.delete_table(u'accounting_record')

        # Deleting model 'Split'
        db.delete_table(u'accounting_split')


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
            'rootAccounts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['accounting.Account']", 'symmetrical': 'False'})
        },
        u'accounting.record': {
            'Meta': {'object_name': 'Record'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'accounting.split': {
            'Meta': {'object_name': 'Split'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounting.Account']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounting.Record']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['accounting']