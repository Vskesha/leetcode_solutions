import unittest
from itertools import permutations
from threading import Event, Thread
from time import sleep


class Foo:
    def __init__(self):
        self.event1 = Event()
        self.event2 = Event()

    def first(self, printFirst: "Callable[[], None]") -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.event1.set()

    def second(self, printSecond: "Callable[[], None]") -> None:
        self.event1.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.event2.set()

    def third(self, printThird: "Callable[[], None]") -> None:
        self.event2.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


class TestFoo(unittest.TestCase):
    def setUp(self):
        self.text = ""

    def printFirst(self):
        # print("first")
        self.text += "first"

    def printSecond(self):
        # print("second")
        self.text += "second"

    def printThird(self):
        # print("third")
        self.text += "third"

    def test_foo_1(self):  # third, second, first

        print("Test Foo ... ")
        numth = ["first", "second", "third"]
        funcs = [self.printFirst, self.printSecond, self.printThird]

        for i, j, k in permutations(range(3), 3):
            print(f"    Test {numth[i]}, {numth[j]}, {numth[k]} ... ", end="")
            foo = Foo()

            th1 = Thread(target=getattr(foo, numth[i]), args=(funcs[i],))
            th2 = Thread(target=getattr(foo, numth[j]), args=(funcs[j],))
            th3 = Thread(target=getattr(foo, numth[k]), args=(funcs[k],))

            th1.start()
            sleep(0.2)
            th2.start()
            sleep(0.2)
            th3.start()

            th1.join()
            th2.join()
            th3.join()

            self.assertEqual(self.text, "firstsecondthird")
            self.text = ""

            print("OK")

        print("Test Passed!")


if __name__ == "__main__":
    unittest.main()
