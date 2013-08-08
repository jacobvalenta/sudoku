from django.db import models
from matrix_field import MatrixField

DIFFICULTY_TYPES = (
    ('e', 'easy'),
    ('n', 'normal'),
    ('h', 'hard'),
    ('x', 'expert')
)

class Puzzel(models.Model):
    puzzel = MatrixField(datatype='int', dimensions=(9,9))
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY_TYPES)