import test


def simplify_path(path: str) -> str:
    result = []
    for el in path.split('/'):
        if el and el != '.' and el != '..':
            result.append(el)
        if el == '..' and result:
            result.pop()
    return '/' + '/'.join(result)


if __name__ == '__main__':
    test.assert_equals(simplify_path('/home/'), '/home')
    test.assert_equals(simplify_path('/../'), '/')
    test.assert_equals(simplify_path('/home//foo/'), '/home/foo')