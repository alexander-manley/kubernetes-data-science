from pyspark.mllib.linalg import Vectors
from pyspark.mllib.linalg.distributed import RowMatrix

rows = sc.parallelize([
    Vectors.sparse(),
    Vectors.dense(),
    Vectors.dense()
])

mat = RowMatrix(rows)
# Compute the top 4 principal components.
# Principal components are stored in a local dense matrix.
pc = mat.computePrincipalComponents(4)

# Project the rows to the linear space spanned by the top 4 principal components.
projected = mat.multiply(pc)
