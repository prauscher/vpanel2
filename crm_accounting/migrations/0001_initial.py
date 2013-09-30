# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Affiliate'
        db.create_table(u'crm_accounting_affiliate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm_contacts.Contact'])),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounting.Account'])),
        ))
        db.send_create_signal(u'crm_accounting', ['Affiliate'])

        # Adding model 'AffiliateAccount'
        db.create_table(u'crm_accounting_affiliateaccount', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('affiliate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm_accounting.Affiliate'])),
            ('iban', self.gf('django.db.models.fields.CharField')(max_length=34)),
        ))
        db.send_create_signal(u'crm_accounting', ['AffiliateAccount'])


    def backwards(self, orm):
        # Deleting model 'Affiliate'
        db.delete_table(u'crm_accounting_affiliate')

        # Deleting model 'AffiliateAccount'
        db.delete_table(u'crm_accounting_affiliateaccount')


    models = {
        u'accounting.account': {
            'Meta': {'object_name': 'Account'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounting.Account']", 'null': 'True', 'blank': 'True'})
        },
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
        u'crm_accounting.affiliate': {
            'Meta': {'object_name': 'Affiliate'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounting.Account']"}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm_contacts.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'crm_accounting.affiliateaccount': {
            'Meta': {'object_name': 'AffiliateAccount'},
            'affiliate': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm_accounting.Affiliate']"}),
            'iban': ('django.db.models.fields.CharField', [], {'max_length': '34'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'crm_contacts.contact': {
            'Meta': {'object_name': 'Contact', '_ormbases': [u'crm.Entity']},
            'emails': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['crm_contacts.Email']", 'symmetrical': 'False'}),
            u'entity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['crm.Entity']", 'unique': 'True', 'primary_key': 'True'}),
            'telephoneNumbers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['crm_contacts.TelephoneNumber']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'crm_contacts.email': {
            'Meta': {'object_name': 'Email'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'crm_contacts.telephonenumber': {
            'Meta': {'object_name': 'TelephoneNumber'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['crm_accounting']