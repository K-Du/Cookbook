# X and Y are two lists, want to sort X based on Y

X.sort(key=dict(zip(X, Y)).get)

# Or

[x for (y,x) in sorted(zip(Y,X), key=lambda pair: pair[0])]
