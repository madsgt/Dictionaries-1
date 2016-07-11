# put your code here.
def wordcount(filename):

    open_file = open(filename)
    word_count = {}
    
    for line in open_file:
        
        line_rstripped = line.rstrip()                  # Remove the extra whitespace from the right of the line
        line_split = line_rstripped.split(" ")          # Split the words by the whitespace

        for word in line_split:                                 # For each word that is split
            word_count[word] = word_count.get(word, 0) + 1      # This line accomplishes two things: 1. Adds each word & count to dictionary
                                                                # 2. Counts the number of occurrences
            

    return word_count



print wordcount("test.txt")