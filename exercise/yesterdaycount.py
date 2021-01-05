# yesterday count homework

# file read
yesterday = open('yesterday.txt', 'r')
yesterday_read = yesterday.read()

# count 'YESTERDAY'
print('YESTERDAY is ', yesterday_read.upper().count('YESTERDAY'))

# count 'Yesterday'
print('Yesterday is ', yesterday_read.count('Yesterday'))

# count 'yesterday'
print('yesterday is ', yesterday_read.lower().count('yesterday'))

yesterday.close()