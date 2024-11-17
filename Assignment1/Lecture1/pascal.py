

def pascal_rec(lst, n):
    if len(lst) > n:
        return lst

    new_line = [1]

    for i in range(1, len(lst)):
        new_line.append(lst[i - 1] + lst[i])

    new_line.append(1)

    return pascal_rec(new_line, n)


def pascal_line(n):
    if n == 1:
        return [1]
    else:
        return pascal_rec([], n)

start, end = 1,7

for i in range(start, end):
  print("  "*(7-i), pascal_line(i))
