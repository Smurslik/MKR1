matrix = [[14, 42, 0],
          [16, 93, 16],
          [47, 0, 89]]


numColumns = len(matrix[0])
columnSum = [0] * numColumns
for row in matrix:
    for i in range(numColumns):
        columnSum[i] += row[i]

sortedColumns = sorted(range(numColumns), key=lambda x: columnSum[x])
sortedarray = [[row[i] for i in sortedColumns] for row in matrix]


print("Сума колонок:", columnSum)
print("Відсортовані колонки")
for row in sortedarray:
    print(row)
