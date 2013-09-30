# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Entity'
        db.create_table(u'crm_entity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('memo', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'crm', ['Entity'])

        # Adding M2M table for field links on 'Entity'
        m2m_table_name = db.shorten_name(u'crm_entity_links')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_entity', models.ForeignKey(orm[u'crm.entity'], null=False)),
            ('to_entity', models.ForeignKey(orm[u'crm.entity'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_entity_id', 'to_entity_id'])

        # Adding M2M table for field tags on 'Entity'
        m2m_table_name = db.shorten_name(u'crm_entity_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('entity', models.ForeignKey(orm[u'crm.entity'], null=False)),
            ('tag', models.ForeignKey(orm[u'crm.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['entity_id', 'tag_id'])

        # Adding model 'Tag'
        db.create_table(u'crm_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'crm', ['Tag'])

        # Adding model 'Process'
        db.create_table(u'crm_process', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'crm', ['Process'])

        # Adding model 'Filter'
        db.create_table(u'crm_filter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=70)),
        ))
        db.send_create_signal(u'crm', ['Filter'])

        # Adding model 'Invariant'
        db.create_table(u'crm_invariant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Filter'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'crm', ['Invariant'])


    def backwards(self, orm):
        # Deleting model 'Entity'
        db.delete_table(u'crm_entity')

        # Removing M2M table for field links on 'Entity'
        db.delete_table(db.shorten_name(u'crm_entity_links'))

        # Removing M2M table for field tags on 'Entity'
        db.delete_table(db.shorten_name(u'crm_entity_tags'))

        # Deleting model 'Tag'
        db.delete_table(u'crm_tag')

        # Deleting model 'Process'
        db.delete_table(u'crm_process')

        # Deleting model 'Filter'
        db.delete_table(u'crm_filter')

        # Deleting model 'Invariant'
        db.delete_table(u'crm_invariant')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'crm.entity': {
            'Meta': {'object_name': 'Entity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'links': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'links_rel_+'", 'blank': 'True', 'to': u"orm['crm.Entity']"}),
            'memo': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['crm.Tag']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'crm.filter': {
            'Meta': {'object_name': 'Filter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        u'crm.invariant': {
            'Meta': {'object_name': 'Invariant'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'filter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Filter']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'crm.process': {
            'Meta': {'object_name': 'Process'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'crm.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['crm']