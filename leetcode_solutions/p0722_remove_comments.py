from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:

        lines = "\n".join(source) + "\n"
        i, ll = 0, len(lines) - 1
        res = []
        while i < ll:
            ch = lines[i]
            if ch == "/" and lines[i + 1] == "/":
                i = lines.find("\n", i + 2)
            elif ch == "/" and lines[i + 1] == "*":
                i = lines.find("*/", i + 2) + 2
            else:
                res.append(ch)
                i += 1
        return [line for line in "".join(res).split("\n") if line]


class Solution1:
    def removeComments(self, source: List[str]) -> List[str]:

        lines = "\n".join(source) + "\n"
        i = 0
        while i < len(lines) - 1:
            if lines[i : i + 2] == "//":
                ei = lines.find("\n", i + 2)
                lines = lines[:i] + lines[ei:]
            elif lines[i : i + 2] == "/*":
                ei = lines.find("*/", i + 2)
                lines = lines[:i] + lines[ei + 2 :]
            else:
                i += 1
        return [line for line in lines.split("\n") if line]


class Solution2:
    def removeComments(self, source: List[str]) -> List[str]:
        ml = None
        i, ls = 0, len(source)

        while i < ls:
            line = source[i]
            if ml is not None:
                ie = line.find("*/")
                if ie == -1:
                    source[i] = ""
                    i += 1
                else:
                    source[ml] += line[ie + 2 :]
                    source[i] = ""
                    i = ml
                    ml = None
            else:
                prev = ""
                for fi, ch in enumerate(line):
                    if prev == "/":
                        if ch == "/":
                            source[i] = line[: fi - 1]
                            i += 1
                            break
                        elif ch == "*":
                            ie = line.find("*/", fi + 1)
                            if ie == -1:
                                source[i] = line[: fi - 1]
                                ml = i
                                i += 1
                                break
                            else:
                                source[i] = line[: fi - 1] + line[ie + 2 :]
                                break
                    prev = ch
                else:
                    i += 1

        source = [line for line in source if line]
        return source


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.removeComments(
        source=[
            "/*Test program */",
            "int main()",
            "{ ",
            "  // variable declaration ",
            "int a, b, c;",
            "/* This is a test",
            "   multiline  ",
            "   comment for ",
            "   testing */",
            "a = b + c;",
            "}",
        ]
    ) == ["int main()", "{ ", "  ", "int a, b, c;", "a = b + c;", "}"]
    print("OK")

    print("Test 2... ", end="")
    assert sol.removeComments(
        source=["a/*comment", "line", "more_comment*/b"]
    ) == ["ab"]
    print("OK")

    print("Test 3... ", end="")
    assert sol.removeComments(source=["a//*b//*c", "blank", "d//*e/*/f"]) == [
        "a",
        "blank",
        "d",
    ]
    print("OK")


if __name__ == "__main__":
    test()
