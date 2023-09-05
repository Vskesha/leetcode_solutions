from functools import lru_cache
from collections import deque


class Solution:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
        skill_pl = [set() for _ in req_skills]
        skills = {skill: pos for pos, skill in enumerate(req_skills)}

        for i, sks in enumerate(people):
            for sk in sks:
                skill_pl[skills[sk]].add(i)

        queue = deque([(skill_pl, [])])

        while queue:
            top_skills, curr_group = queue.popleft()
            rarest_skill_possessors = min(top_skills, key=len)
            for person_id in rarest_skill_possessors:
                remaining_skills = [possessor for possessor in top_skills if person_id not in possessor]
                if not remaining_skills:
                    return curr_group + [person_id]
                queue.append((remaining_skills, curr_group + [person_id]))


# recursive dp solution
class Solution1:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
        n = len(people)
        m = len(req_skills)
        skills_ids = {req_skills[i]: i for i in range(m)}

        people_masks = [0] * n
        for i in range(n):
            for skill in people[i]:
                people_masks[i] |= 1 << skills_ids[skill]

        @lru_cache(None)
        def find_team_mask(skills_mask):
            if skills_mask == 0:
                return 0

            min_people_mask = (1 << n) - 1
            for i in range(n):
                smaller_mask = skills_mask & ~people_masks[i]
                if smaller_mask != skills_mask:
                    people_mask = find_team_mask(smaller_mask) | (1 << i)
                    if people_mask.bit_count() < min_people_mask.bit_count():
                        min_people_mask = people_mask
            return min_people_mask

        answer_mask = find_team_mask((1 << m) - 1)
        ans = []
        for i in range(n):
            if (answer_mask >> i) & 1:
                ans.append(i)
        return ans


# iterative solution
class Solution2:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
        n = len(people)
        m = len(req_skills)
        skills_ids = {req_skills[i]: i for i in range(m)}

        people_masks = [0] * n
        for i in range(n):
            for skill in people[i]:
                people_masks[i] |= 1 << skills_ids[skill]

        dp = [(1 << n) - 1] * (1 << m)
        dp[0] = 0

        for skills_mask in range(1, (1 << m)):
            for i in range(n):
                smaller_mask = skills_mask & ~people_masks[i]
                if smaller_mask != skills_mask:
                    people_mask = dp[smaller_mask] | (1 << i)
                    if people_mask.bit_count() < dp[skills_mask].bit_count():
                        dp[skills_mask] = people_mask

        answer_mask = dp[(1 << m) - 1]
        ans = []
        for i in range(n):
            if (answer_mask >> i) & 1:
                ans.append(i)
        return ans


def main():
    sol = Solution()
    print(' [0, 2]\n', sol.smallestSufficientTeam(req_skills=["java", "nodejs", "reactjs"],
                                                      people=[["java"], ["nodejs"], ["nodejs", "reactjs"]]))
    print(' [1, 2]\n', sol.smallestSufficientTeam(req_skills=["algorithms", "math", "java",
                                                                  "reactjs", "csharp", "aws"],
                                                      people=[["algorithms", "math", "java"],
                                                              ["algorithms", "math", "reactjs"],
                                                              ["java", "csharp", "aws"],
                                                              ["reactjs", "csharp"],
                                                              ["csharp", "math"],
                                                              ["aws", "java"]]))
    print(' [0, 16]\n', sol.smallestSufficientTeam(req_skills=["hdbxcuzyzhliwv", "uvwlzkmzgis", "sdi",
                                                                 "bztg", "ylopoifzkacuwp", "dzsgleocfpl"],
                                                     people=[["hdbxcuzyzhliwv","dzsgleocfpl"],["hdbxcuzyzhliwv","sdi","ylopoifzkacuwp","dzsgleocfpl"],["bztg","ylopoifzkacuwp"],["bztg","dzsgleocfpl"],["hdbxcuzyzhliwv","bztg"],["dzsgleocfpl"],["uvwlzkmzgis"],["dzsgleocfpl"],["hdbxcuzyzhliwv"],[],["dzsgleocfpl"],["hdbxcuzyzhliwv"],[],["hdbxcuzyzhliwv","ylopoifzkacuwp"],["sdi"],["bztg","dzsgleocfpl"],["hdbxcuzyzhliwv","uvwlzkmzgis","sdi","bztg","ylopoifzkacuwp"],["hdbxcuzyzhliwv","sdi"],["hdbxcuzyzhliwv","ylopoifzkacuwp"],["sdi","bztg","ylopoifzkacuwp","dzsgleocfpl"],["dzsgleocfpl"],["sdi","ylopoifzkacuwp"],["hdbxcuzyzhliwv","uvwlzkmzgis","sdi"],[],[],["ylopoifzkacuwp"],[],["sdi","bztg"],["bztg","dzsgleocfpl"],["sdi","bztg"]]))
    print(' [1, 13, 30, 31, 50, 51]\n', sol.smallestSufficientTeam(req_skills=["hfkbcrslcdjq","jmhobexvmmlyyzk","fjubadocdwaygs","peaqbonzgl","brgjopmm","x","mf","pcfpppaxsxtpixd","ccwfthnjt","xtadkauiqwravo","zezdb","a","rahimgtlopffbwdg","ulqocaijhezwfr","zshbwqdhx","hyxnrujrqykzhizm"],
                                                  people=[["peaqbonzgl","xtadkauiqwravo"],["peaqbonzgl","pcfpppaxsxtpixd","zshbwqdhx"],["x","a"],["a"],["jmhobexvmmlyyzk","fjubadocdwaygs","xtadkauiqwravo","zshbwqdhx"],["fjubadocdwaygs","x","zshbwqdhx"],["x","xtadkauiqwravo"],["x","hyxnrujrqykzhizm"],["peaqbonzgl","x","pcfpppaxsxtpixd","a"],["peaqbonzgl","pcfpppaxsxtpixd"],["a"],["hyxnrujrqykzhizm"],["jmhobexvmmlyyzk"],["hfkbcrslcdjq","xtadkauiqwravo","a","zshbwqdhx"],["peaqbonzgl","mf","a","rahimgtlopffbwdg","zshbwqdhx"],["xtadkauiqwravo"],["fjubadocdwaygs"],["x","a","ulqocaijhezwfr","zshbwqdhx"],["peaqbonzgl"],["pcfpppaxsxtpixd","ulqocaijhezwfr","hyxnrujrqykzhizm"],["a","ulqocaijhezwfr","hyxnrujrqykzhizm"],["a","rahimgtlopffbwdg"],["zshbwqdhx"],["fjubadocdwaygs","peaqbonzgl","brgjopmm","x"],["hyxnrujrqykzhizm"],["jmhobexvmmlyyzk","a","ulqocaijhezwfr"],["peaqbonzgl","x","a","ulqocaijhezwfr","zshbwqdhx"],["mf","pcfpppaxsxtpixd"],["fjubadocdwaygs","ulqocaijhezwfr"],["fjubadocdwaygs","x","a"],["zezdb","hyxnrujrqykzhizm"],["ccwfthnjt","a"],["fjubadocdwaygs","zezdb","a"],[],["peaqbonzgl","ccwfthnjt","hyxnrujrqykzhizm"],["xtadkauiqwravo","hyxnrujrqykzhizm"],["peaqbonzgl","a"],["x","a","hyxnrujrqykzhizm"],["zshbwqdhx"],[],["fjubadocdwaygs","mf","pcfpppaxsxtpixd","zshbwqdhx"],["pcfpppaxsxtpixd","a","zshbwqdhx"],["peaqbonzgl"],["peaqbonzgl","x","ulqocaijhezwfr"],["ulqocaijhezwfr"],["x"],["fjubadocdwaygs","peaqbonzgl"],["fjubadocdwaygs","xtadkauiqwravo"],["pcfpppaxsxtpixd","zshbwqdhx"],["peaqbonzgl","brgjopmm","pcfpppaxsxtpixd","a"],["fjubadocdwaygs","x","mf","ulqocaijhezwfr"],["jmhobexvmmlyyzk","brgjopmm","rahimgtlopffbwdg","hyxnrujrqykzhizm"],["x","ccwfthnjt","hyxnrujrqykzhizm"],["hyxnrujrqykzhizm"],["peaqbonzgl","x","xtadkauiqwravo","ulqocaijhezwfr","hyxnrujrqykzhizm"],["brgjopmm","ulqocaijhezwfr","zshbwqdhx"],["peaqbonzgl","pcfpppaxsxtpixd"],["fjubadocdwaygs","x","a","zshbwqdhx"],["fjubadocdwaygs","peaqbonzgl","x"],["ccwfthnjt"]]))


if __name__ == '__main__':
    main()
