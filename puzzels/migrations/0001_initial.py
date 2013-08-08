# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Puzzel'
        db.create_table('puzzels_puzzel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('puzzel', self.gf('matrix_field.fields.MatrixField')(dimensions=(9, 9), default=None, datatype='int')),
            ('difficulty', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('puzzels', ['Puzzel'])


    def backwards(self, orm):
        # Deleting model 'Puzzel'
        db.delete_table('puzzels_puzzel')


    models = {
        'puzzels.puzzel': {
            'Meta': {'object_name': 'Puzzel'},
            'difficulty': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puzzel': ('matrix_field.fields.MatrixField', [], {'dimensions': '(9, 9)', 'default': 'None', 'datatype': "'int'"})
        }
    }

    complete_apps = ['puzzels']