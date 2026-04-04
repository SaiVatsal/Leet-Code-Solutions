class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText:
            return ""
        cols = len(encodedText) // rows 
        decoded_chars = []
        
        for start_col in range(cols): # col ? cols 
            row, col  = 0 , start_col   
            while row < rows  and col < cols:
                index = (row * cols) + col # formulea
                decoded_chars.append(encodedText[index])
                row += 1
                col += 1
            
        return "" .join(decoded_chars).rstrip()   