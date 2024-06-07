import unittest
from typing import List


class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Trie()
            curr = curr.children[ch]
        curr.is_end = True


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        def get_root(word) -> str:
            curr = trie
            for i, ch in enumerate(word):
                if ch not in curr.children:
                    break
                curr = curr.children[ch]
                if curr.is_end:
                    return word[: i + 1]
            return word

        return " ".join(map(get_root, sentence.split()))


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def test_replace_words1(self):
        print("Test replaceWords 1 ... ", end="")
        self.assertEqual(
            self.sol.replaceWords(
                dictionary=["cat", "bat", "rat"],
                sentence="the cattle was rattled by the battery",
            ),
            "the cat was rat by the bat",
        )
        print("OK")

    def test_replace_words2(self):
        print("Test replaceWords 2 ... ", end="")
        self.assertEqual(
            self.sol.replaceWords(
                dictionary=["a", "b", "c"], sentence="aadsfasf absbs bbab cadsfafs"
            ),
            "a a b c",
        )
        print("OK")

    def test_replace_words3(self):
        print("Test replaceWords 3 ... ", end="")
        self.assertEqual(
            self.sol.replaceWords(
                dictionary=[
                    "e",
                    "k",
                    "c",
                    "harqp",
                    "h",
                    "gsafc",
                    "vn",
                    "lqp",
                    "soy",
                    "mr",
                    "x",
                    "iitgm",
                    "sb",
                    "oo",
                    "spj",
                    "gwmly",
                    "iu",
                    "z",
                    "f",
                    "ha",
                    "vds",
                    "v",
                    "vpx",
                    "fir",
                    "t",
                    "xo",
                    "apifm",
                    "tlznm",
                    "kkv",
                    "nxyud",
                    "j",
                    "qp",
                    "omn",
                    "zoxp",
                    "mutu",
                    "i",
                    "nxth",
                    "dwuer",
                    "sadl",
                    "pv",
                    "w",
                    "mding",
                    "mubem",
                    "xsmwc",
                    "vl",
                    "farov",
                    "twfmq",
                    "ljhmr",
                    "q",
                    "bbzs",
                    "kd",
                    "kwc",
                    "a",
                    "buq",
                    "sm",
                    "yi",
                    "nypa",
                    "xwz",
                    "si",
                    "amqx",
                    "iy",
                    "eb",
                    "qvgt",
                    "twy",
                    "rf",
                    "dc",
                    "utt",
                    "mxjfu",
                    "hm",
                    "trz",
                    "lzh",
                    "lref",
                    "qbx",
                    "fmemr",
                    "gil",
                    "go",
                    "qggh",
                    "uud",
                    "trnhf",
                    "gels",
                    "dfdq",
                    "qzkx",
                    "qxw",
                ],
                sentence="ikkbp miszkays wqjferqoxjwvbieyk gvcfldkiavww "
                         "vhokchxz dvypwyb bxahfzcfanteibiltins ueebf "
                         "lqhflvwxksi dco kddxmckhvqifbuzkhstp wc ytzzlm "
                         "gximjuhzfdjuamhsu gdkbmhpnvy ifvifheoxqlbosfww "
                         "mengfdydekwttkhbzenk wjhmmyltmeufqvcpcxg hthcuovils "
                         "ldipovluo aiprogn nusquzpmnogtjkklfhta klxvvlvyh "
                         "nxzgnrveghc mpppfhzjkbucv cqcft uwmahhqradjtf "
                         "iaaasabqqzmbcig zcpvpyypsmodtoiif qjuiqtfhzcpnmtk "
                         "yzfragcextvx ivnvgkaqs iplazv jurtsyh gzixfeugj "
                         "rnukjgtjpim hscyhgoru aledyrmzwhsz xbahcwfwm hzd "
                         "ygelddphxnbh rvjxtlqfnlmwdoezh zawfkko "
                         "iwhkcddxgpqtdrjrcv bbfj mhs nenrqfkbf spfpazr "
                         "wrkjiwyf cw dtd cqibzmuuhukwylrnld dtaxhddidfwqs "
                         "bgnnoxgyynol hg dijhrrpnwjlju muzzrrsypzgwvblf "
                         "zbugltrnyzbg hktdviastoireyiqf qvufxgcixvhrjqtna "
                         "ipfzhuvgo daee r nlipyfszvxlwqw yoq "
                         "dewpgtcrzausqwhh qzsaobsghgm ichlpsjlsrwzhbyfhm "
                         "ksenb bqprarpgnyemzwifqzz oai pnqottd nygesjtlpala "
                         "qmxixtooxtbrzyorn gyvukjpc s mxhlkdaycskj "
                         "uvwmerplaibeknltuvd ocnn frotscysdyclrc "
                         "ckcttaceuuxzcghw pxbd oklwhcppuziixpvihihp",
            ),
            "i miszkays w gvcfldkiavww v dvypwyb bxahfzcfanteibiltins ueebf "
            "lqhflvwxksi dc k w ytzzlm gximjuhzfdjuamhsu gdkbmhpnvy i "
            "mengfdydekwttkhbzenk w h ldipovluo a nusquzpmnogtjkklfhta k "
            "nxzgnrveghc mpppfhzjkbucv c uwmahhqradjtf i z q yzfragcextvx i i "
            "j gzixfeugj rnukjgtjpim h a x h ygelddphxnbh rvjxtlqfnlmwdoezh z "
            "i bbfj mhs nenrqfkbf spfpazr w c dtd c dtaxhddidfwqs "
            "bgnnoxgyynol h dijhrrpnwjlju muzzrrsypzgwvblf z h q i daee r "
            "nlipyfszvxlwqw yoq dewpgtcrzausqwhh q i k bqprarpgnyemzwifqzz "
            "oai pnqottd nygesjtlpala q gyvukjpc s mxhlkdaycskj "
            "uvwmerplaibeknltuvd ocnn f c pxbd oklwhcppuziixpvihihp"
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
