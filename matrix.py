import math


def matrix_multiplication(a, b):
  colone_a = len(a[0])
  ligne_a = len(a)
  colone_b = len(b[0])
  ligne_b = len(b)
  resulta_matrix = [[j for j in range(colone_b)] for i in range(ligne_a)]

  if colone_a == ligne_b:
    for x in range(ligne_a):
      for y in range(colone_b):
        sum = 0
        for k in range(colone_a):
          sum += a[x][k] * b[k][y]
        resulta_matrix[x][y] = sum
    return resulta_matrix
  else:
    print(
      "les colonnes de la première matrice doivent être égales aux lignes de la deuxième matrice"
    )


def rotationX(angle):
  return [[1, 0, 0], [0, math.cos(angle), -math.sin(angle)],
          [0, math.sin(angle), math.cos(angle)]]


def rotationY(angle):
  return [[math.cos(angle), 0, -math.sin(angle)], [0, 1, 0],
          [math.sin(angle), 0, math.cos(angle)]]


def rotationZ(angle):
  return [[math.cos(angle), -math.sin(angle), 0],
          [math.sin(angle), math.cos(angle), 0], [0, 0, 1]]
