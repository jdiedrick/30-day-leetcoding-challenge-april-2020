class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []: return 0
        m, n = len(matrix), len(matrix[0])
        D = [[0] * n for _ in range(m)]
        V = copy.deepcopy(D)
        H = copy.deepcopy(D)
        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
        ret = 0
        for i in range(m):
            D[i][0] = matrix[i][0]
            H[i][0] = matrix[i][0]
            ret = max(ret, D[i][0])
        
        for j in range(n):
            D[0][j] = matrix[0][j]
            V[0][j] = matrix[0][j]
            ret = max(ret, D[0][j])
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    continue
                D[i][j] = min([D[i - 1][j - 1], V[i - 1][j], H[i][j - 1]]) + 1
                V[i][j] = V[i - 1][j] + 1
                H[i][j] = H[i][j - 1] + 1
                ret = max(ret, D[i][j])
        return ret * ret

