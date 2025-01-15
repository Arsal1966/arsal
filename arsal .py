def word_pattern(pattern, s):
    # Split the string into words
    words = s.split()

    # If lengths don't match, pattern can't hold
    if len(pattern) != len(words):
        return False

    # Dictionaries to map pattern to words and vice versa
    pattern_to_word = {}
    word_to_pattern = {}

    # Iterate through both the pattern and words
    for p, w in zip(pattern, words):
        # Check if this pattern character has a mapping
        if p in pattern_to_word:
            if pattern_to_word[p] != w:  # Mapping mismatch
                return False
        else:
            pattern_to_word[p] = w  # Create a new mapping

        # Check if this word has a mapping
        if w in word_to_pattern:
            if word_to_pattern[w] != p:  # Mapping mismatch
                return False
        else:
            word_to_pattern[w] = p  # Create a new mapping

    return True  # Return true if all mappings are consistent

# Test cases
print(word_pattern("abba", "dog cat cat dog"))  # Expected: True
print(word_pattern("abba", "dog cat cat fish"))  # Expected: False
print(word_pattern("aaaa", "dog cat cat dog"))  # Expected: False
