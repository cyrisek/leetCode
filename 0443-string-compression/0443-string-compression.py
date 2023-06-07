class Solution:
    def compress(self, chars: List[str]) -> int:
        write_index = 0  
        count = 1
        
        for i, char in enumerate(chars[1:], start=1):
            if char == chars[i-1]:
                count += 1
            else:
                chars[write_index] = chars[i-1]
                
                if count > 1:
                    count_str = str(count)
                    for j, digit in enumerate(count_str):
                        chars[write_index + j + 1] = digit 
                    write_index += len(count_str) + 1  
                else:
                    write_index += 1  
                    
                count = 1 
        
        chars[write_index] = chars[-1]
        if count > 1:
            count_str = str(count)
            for j, digit in enumerate(count_str):
                chars[write_index + j + 1] = digit
            write_index += len(count_str) + 1
        else:
            write_index += 1
        
        return write_index