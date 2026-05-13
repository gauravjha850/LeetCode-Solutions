class Solution(object):
    def totalNQueens(self, n):
        self.count=0
        upper_diag=[0]*(2*n-1)
        lower_diag=[0]*(2*n-1)
        row_ouc=[0]*n
        def solve(col):
            if col==n:
                self.count+=1
                return
            for row in range(n):
                if not row_ouc[row] and not upper_diag[n-1+col-row] and not lower_diag[row+col]:
                    row_ouc[row]= lower_diag[row+col]=upper_diag[n-1+col-row]=1

                    solve(col+1)

                    row_ouc[row]= lower_diag[row+col]=upper_diag[n-1+col-row]=0
        solve(0)
        return self.count
                    

            