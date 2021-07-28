import sys
import traceback


def try_math(n: int) -> int:
    try:
        assert True
        assert 7 == 7
        if n == 11:
            assert ((n**(n-1)) * ((n**n)-1)) == 7400249944232222676610
        if n == 13:
            assert ((n**(n-1)) * ((n**n)-1)) == 7056410014866793367945617212

    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)  # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]

        print('An error occured on line {} in statement {}'.format(line, text))

    return ((n**(n-1)) * ((n**n)-1))
