# line 12
instead of a loop, you could use a list comprehension to normalize the words in one go

# line 14
the logic `w.isdigit()` will fail for words like `"4."` or `"3!"` bcz of the punctuation
you should clean the punctuation before splitting the text into words

# line 18
btw, you can use `.get()` here to handle the dict lookup and the "else" case in one line

# no need to copy-paste each other's work
it's obvious anyway :))
