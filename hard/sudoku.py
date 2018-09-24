class Solution(object):
    index = "{},{}"
    
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.available_map = {}
        self.row_map = {}
        self.col_map = {}
        
        self.populate_maps() 
        self.solve()
        
    def populate_maps(self):
        self.populate_avail_and_row_map()                        
        self.populate_col_map()
        
    def populate_avail_and_row_map(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    self.available_map[self.index.format(row, col)] = self.get_avail(row, col)
                elif row+1 in self.row_map:
                    self.row_map[row+1].update(str(self.board[row][col]))   
                else:
                    self.row_map[row+1] = set(str(self.board[row][col]))
                    
    def populate_col_map(self):
        for col in range(9):
            for row in range(9):
                if self.board[row][col] != '.':
                    if col+1 in self.col_map:
                        self.col_map[col+1].update(str(self.board[row][col]))   
                    else:
                        self.col_map[col+1] = set(str(self.board[row][col]))
                    
    def update_maps(self, row, col, num):                
        self.row_map[row+1].update(num) 
        self.col_map[col+1].update(num) 
        
    def remove_from_maps(self, row, col, num):                
        self.row_map[row+1].remove(num) 
        self.col_map[col+1].remove(num) 
                    
    def solve(self):
        row, col = self.get_open_index()
        if row == -1 and col == -1:
            return True
        for num in self.available_map[self.index.format(row, col)]:
            if self.check_safe(row, col, num):
                self.board[row][col] = num
                self.update_maps(row, col, num)
                if self.solve():
                    return True 
                self.board[row][col] = '.'
                self.remove_from_maps(row, col, num)
        return False
        
    def check_safe(self, row, col, num):
        if self.check_row(row, num) and self.check_col(col, num) and self.check_box(row, col, num):
            return True
        return False
    
    def check_row(self, row, num):
        return row+1 in self.row_map and num not in self.row_map[row+1]
    
    def check_col(self, col, num):
        return col+1 in self.col_map and num not in self.col_map[col+1]
    
    def check_box(self, row, col, num):
        boxrow = row - row%3
        boxcol = col - col%3
        for r in range(boxrow, boxrow+3):
            for c in range(boxcol, boxcol+3):
                if self.board[r][c] == num:
                    return False
                
        return True    
                 
    def get_open_index(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return row, col
        return -1, -1 
    
    def get_avail(self, row, col): 
        avail = set(str(x) for x in range(1, 10)) 
        avail = self.get_avail_row(row, avail)
        avail = self.get_avail_col(col, avail)
        avail = self.get_avail_box(row, col, avail)
        return avail
    
    def get_avail_row(self, row, avail):
        for col in range(9):
            if self.board[row][col] != '.':
                if self.board[row][col] in avail: avail.remove(self.board[row][col])
        return avail 
    
    def get_avail_col(self, col, avail):
        for row in range(9):
            if self.board[row][col] != '.':
                if self.board[row][col] in avail: avail.remove(self.board[row][col])
        return avail 
    
    def get_avail_box(self, row, col, avail):
        boxrow = row - row%3
        boxcol = col - col%3
        for r in range(boxrow, boxrow+3):
            for c in range(boxcol, boxcol+3):
                if self.board[r][c] != '.':
                    if self.board[r][c] in avail: avail.remove(self.board[r][c])
        return avail 
