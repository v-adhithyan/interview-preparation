"""Global analytics interview question."""
# Given two words, convert one word to another.
# You can perform only one operation at a time.
# List of allowed operations replace, insert, delete
from difflib import SequenceMatcher
from collections import namedtuple

word_1 = "ticket"
word_2 = "bucket"

sequence_matcher = SequenceMatcher(a=word_1, b=word_2)

# To get matching sequences in both words
#
# > [Match(a=2, b=2, size=4), Match(a=6, b=6, size=0)]
matching_blocks = sequence_matcher.get_matching_blocks()

# to convert the word_1 to word_2, we need to get list of operations
# like insert, delete, replace etc
# use s.get_opcodes()
# Returns a list containing tuples
# Each tuple has five values
# index 0 -> operation to perform ex: replace
# index 1 -> starting index from word 1
# index 2 -> ending index from word 1
# index 3 -> starting index from word 2
# index 4 -> ending index from word 2
# Sample output: [('replace', 0, 2, 0, 2), ('equal', 2, 6, 2, 6)]
# The tuple at index 0 in the above when read in plain english is as follows
# replace characters in word_1 from index 0 to 1 with characters in word_2 from
# index 0 to 1
_opcodes = sequence_matcher.get_opcodes()
output_word = ""
steps = namedtuple(
    'steps', 'operation word1_start word1_end word2_start word2_end')
for _opcode in _opcodes:
    current_step = steps(operation=_opcode[0], word1_start=_opcode[1],
                         word1_end=_opcode[2],
                         word2_start=_opcode[3], word2_end=_opcode[4])
    if current_step.operation == "replace":
        pass
    if current_step.operation == "equal":
        pass
    if current_step.operation == "insert":
        pass
    if current_step.operation == "delete":
        pass
