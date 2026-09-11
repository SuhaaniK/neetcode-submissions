from typing import List 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                row_tag = (r,val)
                col_tag = (val,c)
                box_tag = (r//3, c//3, val)

                if row_tag in seen or col_tag in seen or box_tag in seen:
                    return False

                seen.add(row_tag)
                seen.add(col_tag)
                seen.add(box_tag)

        return True
        