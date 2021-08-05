from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

print("----------Working with Counter------------")

test_str = 'aaaaabbbccccc'
counter_var = Counter(test_str)
print(counter_var)
print(counter_var.most_common(n=1)[0])
print(list(counter_var.elements()))

print("---------Working with namedtuple-----------")

Point = namedtuple(typename='Point', field_names='x,y')
pt = Point(1, 4)
print(pt)
print(pt.x, pt.y)

print("---------Working with OrderedDict-----------")

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

print("---------Working with defaultdict-----------")

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d)

print("---------Working with deque-----------")

d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
d.popleft()

print(d)
