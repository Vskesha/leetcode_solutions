def brace_expansion_ii(expression: str) -> list[str]:
    stack = []
    setex, curex = set(), {''}

    for c in expression:
        if c == '{':
            stack.append((setex, curex))
            setex, curex = set(), {''}

        elif c == '}':
            totex = setex.union(curex)
            setex, curex = stack.pop()
            curex = {s1 + s2 for s1 in curex for s2 in totex}

        elif c == ',':
            setex.update(curex)
            curex = {''}

        else:
            curex = {s1 + c for s1 in curex}

    return sorted(curex)


def brace_expansion_ii0(expr: str) -> list[str]:
    def rec():
        nonlocal i
        res = set()
        if expr[i] == '{':
            i += 1
            res.update(rec())
            while i < le and expr[i] == ',':
                i += 1
                res.update(rec())
            i += 1
        elif expr[i].isalpha():
            w = ''
            while i < le and expr[i].isalpha():
                w += expr[i]
                i += 1
            res.add(w)
        if i < le and (expr[i] == '{' or expr[i].isalpha()):
            res = {a + b for b in rec() for a in res}
        return res

    i = 0
    le = len(expr)
    return sorted(rec())


def brace_expansion_ii1(s: str) -> list[str]:
    def getWord():
        nonlocal i
        word = ""
        while i < len(s) and s[i].isalpha():
            word += s[i]
            i += 1
        return word

    def dfs():
        nonlocal i
        res = set()
        if s[i] == '{':
            i += 1
            res.update(dfs())
            while i < len(s) and s[i] == ',':
                i += 1
                res.update(dfs())
            i += 1
        elif s[i].isalpha():
            res.add(getWord())

        while i < len(s) and (s[i] == '{' or s[i].isalpha()):
            res = {w + a for a in dfs() for w in res}
        return res

    i = 0
    return sorted(dfs())


def brace_expansion_ii2(expression: str) -> list[str]:
    def divis(exp):
        # delete first { and last } if 'exp' surrended with {}
        if exp[0] == '{' and exp[-1] == '}':
            closed = 0
            for i, c in enumerate(exp):
                if c == '{':
                    closed += 1
                elif c == '}':
                    closed -= 1
                if not closed:
                    closed = i
                    break
            if closed == len(exp) - 1:
                exp = exp[1:-1]

        # if no brackets in 'exp' return splitted by comma set
        if '{' not in exp:
            return set(exp.split(','))

        # divide 'exp' on two parts that was separated with comma
        # and return their joined set
        left, right = '', ''
        brackets = 0
        for i, c in enumerate(exp):
            if c == '{':
                brackets += 1
            elif c == '}':
                brackets -= 1
            elif c == ',' and brackets == 0:
                left = exp[:i]
                right = exp[i + 1:]
                break
        if left:
            l_set = divis(left)
            r_set = divis(right)
            return l_set | r_set

        # divide 'exp' on two parts and return their product
        if exp[0] == '{':
            i = 0
            for j, c in enumerate(exp):
                if c == '{':
                    i += 1
                elif c == '}':
                    i -= 1
                if not i:
                    i = j + 1
        else:
            i = exp.index('{')
        left = exp[:i]
        right = exp[i:]
        l_set = divis(left)
        r_set = divis(right)
        return {a + b for a in l_set for b in r_set}

    return sorted(list(divis(expression)))


if __name__ == '__main__':
    print('["ac","ad","ae","bc","bd","be"] ===', brace_expansion_ii("{a,b}{c,{d,e}}"))
    print('["a","ab","ac","z"] ===', brace_expansion_ii("{{a,z},a{b,c},{ab,z}}"))
    print("['nga', 'ngia', 'ngo', 'ngw', 'ngx', 'noa', 'noia', 'noo', 'now', 'nox', 'nua', 'nuia', 'nuo', 'nuw', 'nux'] ===",
          brace_expansion_ii("n{g,{u,o}}{a,{x,ia,o},w}"))
