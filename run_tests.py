import unittest

if __name__ == "__main__":
    # Discover all the tests in the `leetcode_solutions` directory
    test_loader = unittest.defaultTestLoader
    test_suite = test_loader.discover("leetcode_solutions", pattern="*.py")

    # Run tests using the custom runner
    runner = unittest.TextTestRunner(
        verbosity=2
    )  # verbosity=2 gives detailed output
    runner.run(test_suite)
