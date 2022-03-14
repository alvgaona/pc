# %% Print literal
print("Today we're studying built-in functions")

# %% Print variable
message = "Today we're studying built-in functions."

print(message)

# %% Concat and print
print("Today we're studying " + "programming")

# %% Format string opt. 1
message = "programming"

print("Today we're studying %s" % message)

# %% Format with f-strings
message = "conditionals"

print(f"Today we're studying {message}")

# %% Format with format
today = "Today"
were = "we're"
studying = "studying"
strings = "strings"

print("{} {} {} {}".format(today, were, studying, strings))
