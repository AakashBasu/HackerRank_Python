# a = 'bcaBCA2314'
in_word = input()
# in_word = 'Sorting1234'
final_word = ''.join(sorted([c for c in in_word if c.islower()])+sorted([c for c in in_word if c.isupper()]))
digits = sorted([c for c in in_word if c.isnumeric()])
next_dig = ''.join([c for c in digits if int(c) % 2 == 1] + [c for c in digits if int(c) % 2 == 0])
final_word = final_word+next_dig
print(final_word)
