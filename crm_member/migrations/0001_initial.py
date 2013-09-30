# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Membership'
        db.create_table(u'crm_member_membership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'crm_member', ['Membership'])

        # Adding model 'Member'
        db.create_table(u'crm_member_member', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm_contacts.Contact'])),
            ('membership', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm_member.Membership'])),
            ('joinDate', self.gf('django.db.models.fields.DateField')()),
            ('resignationDate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'crm_member', ['Member'])


    def backwards(self, orm):
        # Deleting model 'Membership'
        db.delete_table(u'crm_member_membership')

        # Deleting model 'Member'
        db.delete_table(u'crm_member_member')


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
        },
        u'crm_member.member': {
            'Meta': {'object_name': 'Member'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm_contacts.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joinDate': ('django.db.models.fields.DateField', [], {}),
            'membership': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm_member.Membership']"}),
            'resignationDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'crm_member.membership': {
            'Meta': {'object_name': 'Membership'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['crm_member']