from typing import Any


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

    def __init__(cls, *args, **kwargs) -> None:
        ltc = len(cls.test_cases)
        for i, case in enumerate(cls.test_cases):
            target_class = case["class"]
            cls_init_args = case.get("cls_init_args", [])
            cls_init_kwargs = case.get("cls_init_kwargs", {})
            obj = target_class(*cls_init_args, **cls_init_kwargs)
            # print(target_class.__name__)
            lcm = len(case["class_methods"])
            for j in range(lcm):
                setattr(
                    cls,
                    (
                        f"test_{target_class.__name__}_"
                        f"{i + 1:0>{len(str(ltc + 1))}}_"
                        f"{j + 1:0>{len(str(lcm + 1))}}"
                    ),
                    cls.get_test_method(obj, i, j),
                )
        super().__init__(*args, **kwargs)

    @staticmethod
    def get_test_method(
            obj: Any,
            test_case_idx: int,
            method_idx: int
    ) -> callable:
        def test_method(instance: Any) -> None:
            test_case = instance.test_cases[test_case_idx]
            ltc = len(instance.test_cases)

            command = test_case["class_methods"][method_idx]
            lcm = len(test_case["class_methods"])

            args_list = test_case.get("args", [])
            arguments = (
                args_list[method_idx]
                if len(args_list) > method_idx
                else []
            )

            kwargs_list = test_case.get("kwargs", [])
            kwarguments = (
                kwargs_list[method_idx]
                if len(kwargs_list) > method_idx
                else {}
            )

            obj_method = getattr(obj, command)
            result = obj_method(*arguments, **kwarguments)
            expected = test_case["expected"][method_idx]

            amethods = test_case.get("assert_methods", [])
            assert_method = (
                amethods[method_idx]
                if len(amethods) > method_idx
                else "assertEqual"
            )

            info_str = (
                f"Test {test_case_idx + 1:0>{len(str(ltc + 1))}}-"
                f"{method_idx + 1:0>{len(str(lcm + 1))}}."
                f" {obj.__class__.__name__}.{command}("
            )
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
