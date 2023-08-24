class Solution:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        def get_words(i):
            curr_line = []
            curr_length = 0

            while i < len(words) and curr_length + len(words[i]) <= max_width:
                curr_line.append(words[i])
                curr_length += len(words[i]) + 1
                i += 1
            
            return curr_line
        
        def create_line(line, i):
            base_length = -1

            for word in line:
                base_length += len(word) + 1
            
            extra_spaces = max_width - base_length

            if len(line) == 1 or i == len(words):
                return " ".join(line) + " " * extra_spaces
            
            word_count = len(line) - 1
            spaces_per_word = extra_spaces // word_count
            needs_extra_space = extra_spaces % word_count

            for j in range(needs_extra_space):
                line[j] += " "
            
            for j in range(word_count):
                line[j] += " " * spaces_per_word
            
            return " ".join(line)
        
        res = []
        i = 0

        while i < len(words):
            curr_line = get_words(i)
            i += len(curr_line)
            res.append(create_line(curr_line, i))
        
        return res