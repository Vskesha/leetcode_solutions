class TestMeta(type):
    """
    Metaclass for testing classes.
    This metaclass creates test methods for each class_method in the
    list of "class_methods" in all test_cases.

    Each TestClass that inherits from this metaclass should define
    a class variable `test_cases` with a list of test cases like:

    test_cases = [
        {
            "class": Solution,
            "cls_init_args": [],
            "cls_init_kwargs": dict(),
            "class_methods": ["method_name", "another_method_name", ...],
            "args": [[arg1, arg2, ...], [arg1, arg2, ...], ...],
            "kwargs": [{kwarg1:val1, kwarg2:val2,...}, ...],
            "expected": [expectedResult1, expectedResult2, ...],
            "assert_methods": ["assertMethod1", "assertMethod2", ...],
        },
    ]

    "cls_init_args" are optional (empty list will be used if not provided).
    "cls_init_kwargs" are optional (empty dict will be used if not provided).
    "arguments" are optional (empty list will be used if not provided).
    "kwarguments" are optional (empty dict will be used if not provided).
    "assert_methods" are optional (TestCase.assertEqual() is used by default).

    You can also define your own assert methods in your class that uses this
    "TestMeta" and inherited from "unittest.TestCase"
    """

    test_cases = []

    def __init__(self, *args, **kwargs):
        ltc = len(self.test_cases)
        for i, case in enumerate(self.test_cases):
            target_class = case["class"]
            cls_init_args = case.get("cls_init_args", [])
            cls_init_kwargs = case.get("cls_init_kwargs", {})
            obj = target_class(*cls_init_args, **cls_init_kwargs)
            # print(target_class.__name__)
            lcm = len(case["class_methods"])
            for j in range(lcm):
                setattr(
                    self,
                    f"test_{target_class.__name__}_{i + 1:0>{len(str(ltc + 1))}}_{j + 1:0>{len(str(lcm + 1))}}",
                    self.get_test_method(obj, i, j),
                )
        super().__init__(*args, **kwargs)

    @staticmethod
    def get_test_method(obj, i, j):
        def test_method(instance):
            test_case = instance.test_cases[i]
            ltc = len(instance.test_cases)

            command = test_case["class_methods"][j]
            lcm = len(test_case["class_methods"])

            args_list = test_case.get("args", [])
            arguments = args_list[j] if len(args_list) > j else []

            kwargs_list = test_case.get("kwargs", [])
            kwarguments = kwargs_list[j] if len(kwargs_list) > j else {}

            obj_method = getattr(obj, command)
            result = obj_method(*arguments, **kwarguments)
            expected = test_case["expected"][j]

            amethods = test_case.get("assert_methods", [])
            assert_method = amethods[j] if len(amethods) > j else "assertEqual"

            info_str = f"Test {i + 1:0>{len(str(ltc + 1))}}-{j + 1:0>{len(str(lcm + 1))}}. {obj.__class__.__name__}.{command}("
            # info_str += ", ".join(f"{arg}" for arg in arguments)
            # if arguments and kwarguments:
            #     info_str += ", "
            # info_str += ", ".join(f"{k}={v}" for k, v in kwarguments.items())
            info_str += ") ... "
            print(info_str, end="")
            getattr(instance, assert_method)(result, expected)
            print("OK")

        return test_method


"""
Example of test class using "TestMeta":

import unittest

from leetcode_solutions._test_meta import TestMeta


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "cls_init_args": [],
            "cls_init_kwargs": dict(),
            "class_methods": ["class_method"],
            "args": [[], ],
            "kwargs": [
                dict(),
            ],
            "expected": [],
            "assert_methods": ["assertMethod"],
        },
    ]


if __name__ == '__main__':
    unittest.main()
    
"""