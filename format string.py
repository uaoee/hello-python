
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.5%}'.format(yes_votes, percentage))

s='hello world'
str(s)
repr(s)
str(1/7)
x=10*3.25
y=200*200
s= 'The value of x is ' + repr(x) + '. and y is' + repr(y) + '...'
print(s)
