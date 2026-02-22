'''
#1
def squaresofnums(n):
    c = 1
    while c <= n:
        yield c*c
        c += 1 

n = int(input())
for i in squaresofnums(n):
    print(i)

#2
def even_numbers(n):
    for i in range(0, n+1, 2):
        yield str(i)

n = int(input())
first = True
for i in even_numbers(n):
    if not first:
        print(",", end = "")
    print(i, end = "")
    first = False

#3
def divisible(n):
    c = 0
    while c <= n:
        if c % 3 == 0 and c % 4 == 0:
            yield c
        c+=1

n = int(input())
for num in divisible(n):
    print(num, end = " ")

#4
def squares(a,b):
    while a <= b:
        yield a*a
        a+=1

a, b = map(int, input().split())
for s in squares(a,b):
    print(s)

#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for i in countdown(n):
    print(i)

#6
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

n = int(input())
gen = fibonacci()

result = [str(next(gen)) for _ in range(n)]
print(",".join(result))

#7
class Reverse:
    def __init__(self, s):
        self.s = s
        self.l = len(self.s)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.l == 0:
            raise StopIteration
        self.l -= 1
        return self.s[self.l] 

s = input()
rev = Reverse(s)
for i in rev:
    print(i, end = "")


#8
def Prime_nums(n):
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        
        if is_prime:
            yield i
        
n = int(input())
for x in Prime_nums(n):
    print(x, end = " ")



#9
def sqoftwo(n):
    for i in range(n+1):
        yield pow(2, i)

n = int(input())
for i in sqoftwo(n):
    print(i, end = " ")

#10
def cycle(a, k):
    yield a*k

a = list(input().split())
k = int(input())
for i in cycle(a, k):
    print(*i)

#11
import json

def apply_patch(source, patch):
    for key in patch:
        if patch[key] == None:
            if key in source:
                del source[key]
        elif key in source and isinstance(source[key], dict) and isinstance(patch[key], dict):
            apply_patch(source[key], patch[key])
        else:
            source[key] = patch[key]
    return source

source = json.loads(input())
patch = json.loads(input())

result = apply_patch(source, patch)
print(json.dumps(result, sort_keys = True, separators =(',', ':')))


#12
import json

MISSING = object()

def to_json_literal(v):
    if v is MISSING:
        return "<missing>"
    return json.dumps(v, separators=(",", ":"))

def deep_diff(a, b, path="", out=None):
    if out is None:
        out = []

    keys = sorted(set(a.keys()) | set(b.keys()))
    for k in keys:
        va = a.get(k, MISSING)
        vb = b.get(k, MISSING)

        new_path = f"{path}.{k}" if path else k

        if va is MISSING or vb is MISSING:
            out.append((new_path, f"{new_path} : {to_json_literal(va)} -> {to_json_literal(vb)}"))
            continue

        if isinstance(va, dict) and isinstance(vb, dict):
            deep_diff(va, vb, new_path, out)
            continue

        if va != vb:
            out.append((new_path, f"{new_path} : {to_json_literal(va)} -> {to_json_literal(vb)}"))

    return out


A = json.loads(input().strip())
B = json.loads(input().strip())

diffs = deep_diff(A, B)

if not diffs:
    print("No differences")
else:
    for _, line in sorted(diffs, key=lambda x: x[0]):
        print(line)




#13
import json

J = json.loads(input())
q = int(input())

for _ in range(q):
    path = input().strip()

    parts = path.replace("[", ".").replace("]", "").split(".")
    parts = [p for p in parts if p != ""]              
    tokens = [int(p) if p.isdigit() else p for p in parts]

    cur = J
    ok = True

    for t in tokens:
        try:
            cur = cur[t]
        except (KeyError, IndexError, TypeError):
            ok = False
            break

    if not ok:
        print("NOT_FOUND")
    else:
        print(json.dumps(cur, separators=(',', ':')))

'''
#14

'''
#17
r = int(input())
x1, y1 = map(int, input().split()) 
x2, y2 = map(int, input().split()) 
'''