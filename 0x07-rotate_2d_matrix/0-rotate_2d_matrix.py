#!/usr/bin/python3
"""
Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
  """rotates the 2d matrix clockwise 90deg"""
  mat =[]
  col = 0
  while col < len(matrix):
      rotated_row =[]
      for row in matrix:
          rotated_row.append(row[col])
          mat.append(rotated_row)
    col += 1
    matrix = mat
