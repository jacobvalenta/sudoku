# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Puzzel.puzzel'
        db.delete_column('puzzels_puzzel', 'puzzel')

        # Adding field 'Puzzel.grid'
        db.add_column('puzzels_puzzel', 'grid',
                      self.gf('matrix_field.fields.MatrixField')(dimensions=(9, 9), default='', datatype='int'),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Puzzel.puzzel'
        raise RuntimeError("Cannot reverse this migration. 'Puzzel.puzzel' and its values cannot be restored.")
        # Deleting field 'Puzzel.grid'
        db.delete_column('puzzels_puzzel', 'grid')


    models = {
        'puzzels.puzzel': {
            'Meta': {'object_name': 'Puzzel'},
            'difficulty': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'grid': ('matrix_field.fields.MatrixField', [], {'dimensions': '(9, 9)', 'default': 'None', 'datatype': "'int'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['puzzels']