# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'crm_contacts_contact', (
            (u'entity_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['crm.Entity'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'crm_contacts', ['Contact'])

        # Adding M2M table for field telephoneNumbers on 'Contact'
        m2m_table_name = db.shorten_name(u'crm_contacts_contact_telephoneNumbers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contact', models.ForeignKey(orm[u'crm_contacts.contact'], null=False)),
            ('telephonenumber', models.ForeignKey(orm[u'crm_contacts.telephonenumber'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contact_id', 'telephonenumber_id'])

        # Adding M2M table for field emails on 'Contact'
        m2m_table_name = db.shorten_name(u'crm_contacts_contact_emails')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contact', models.ForeignKey(orm[u'crm_contacts.contact'], null=False)),
            ('email', models.ForeignKey(orm[u'crm_contacts.email'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contact_id', 'email_id'])

        # Adding model 'NaturalPerson'
        db.create_table(u'crm_contacts_naturalperson', (
            (u'contact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['crm_contacts.Contact'], unique=True, primary_key=True)),
            ('givenName', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('surName', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('birthDay', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'crm_contacts', ['NaturalPerson'])

        # Adding model 'ArtificialPerson'
        db.create_table(u'crm_contacts_artificialperson', (
            (u'contact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['crm_contacts.Contact'], unique=True, primary_key=True)),
            ('legalName', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('contactGivenName', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('contactSurName', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'crm_contacts', ['ArtificialPerson'])

        # Adding model 'TelephoneNumber'
        db.create_table(u'crm_contacts_telephonenumber', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
        ))
        db.send_create_signal(u'crm_contacts', ['TelephoneNumber'])

        # Adding model 'Email'
        db.create_table(u'crm_contacts_email', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
        ))
        db.send_create_signal(u'crm_contacts', ['Email'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'crm_contacts_contact')

        # Removing M2M table for field telephoneNumbers on 'Contact'
        db.delete_table(db.shorten_name(u'crm_contacts_contact_telephoneNumbers'))

        # Removing M2M table for field emails on 'Contact'
        db.delete_table(db.shorten_name(u'crm_contacts_contact_emails'))

        # Deleting model 'NaturalPerson'
        db.delete_table(u'crm_contacts_naturalperson')

        # Deleting model 'ArtificialPerson'
        db.delete_table(u'crm_contacts_artificialperson')

        # Deleting model 'TelephoneNumber'
        db.delete_table(u'crm_contacts_telephonenumber')

        # Deleting model 'Email'
        db.delete_table(u'crm_contacts_email')


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
        u'crm_contacts.artificialperson': {
            'Meta': {'object_name': 'ArtificialPerson', '_ormbases': [u'crm_contacts.Contact']},
            'contactGivenName': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'contactSurName': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['crm_contacts.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'legalName': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
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
        u'crm_contacts.naturalperson': {
            'Meta': {'object_name': 'NaturalPerson', '_ormbases': [u'crm_contacts.Contact']},
            'birthDay': ('django.db.models.fields.DateField', [], {}),
            u'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['crm_contacts.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'givenName': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'surName': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'crm_contacts.telephonenumber': {
            'Meta': {'object_name': 'TelephoneNumber'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['crm_contacts']