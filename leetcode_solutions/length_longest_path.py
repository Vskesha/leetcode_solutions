def length_longest_path(inp: str) -> int:
    max_len = 0
    lens = []  #stack for storing lengths
    lines  = inp.splitlines()
    
    for line in lines:
        tabs = line.count('\t')
        len_line = len(line) - tabs + 1
        lens = lens[:tabs] + [len_line]
        if '.' in line:
            max_len = max(max_len, sum(lens) - 1)
        
    return max_len


if __name__ == '__main__':
    print('20 ===', length_longest_path("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
    print('32 ===', length_longest_path("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
    print('0 ===', length_longest_path('a'))
    