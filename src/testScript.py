__author__ = '60923'
from getsnaps import get_release
import unittest


class Test_case(unittest.TestCase):

    list1 = [('hk.com.hit.ngeni', 'ngen-cbo', '12.3.0-1.8-SNAPSHOT'), ('hk.com.hit.ngeni', 'ngen-cbo', '12.3.0-1.7-SNAPSHOT'), ('hk.com.hit.ngeni', 'ngen-dmc', '12.3.0-1.6-SNAPSHOT')]
    list2 = [('hk.com.hit.ngeni', 'ngen-cbo', '12.3-1.3'), ('hk.com.hit.ngeni', 'ngen-cbo', '12.3-1.2'), ('hk.com.hit.ngeni', 'ngen-cbo', '11.0')]
    list3 = [('hk.com.hit.ngeni', 'ngen-cbo', '5.1-1.3'), ('hk.com.hit.ngeni', 'ngen-cbo', '5.1-1.0'), ('hk.com.hit.ngeni', 'ngen-dmc', '11.0')]

    test1 = get_release(list1)
    test2 = get_release(list2)
    test3 = get_release(list3)

    test1_expected = {'hk.com.hit.ngeni_ngen-dmc': set(['12.3.0-1.6-SNAPSHOT']), 'hk.com.hit.ngeni_ngen-cbo': set(['12.3.0-1.8-SNAPSHOT'])}
    test2_expected = {'hk.com.hit.ngeni_ngen-cbo': set(['12.3-1.3', '11.0'])}
    test3_expected = {'hk.com.hit.ngeni_ngen-cbo': set(['5.1-1.3']), 'hk.com.hit.ngeni_ngen-dmc': set(['11.0'])}

    def test_useful(self):
        self.assertDictEqual(self.test1_expected, self.test1)

    def test_useful1(self):
        self.assertDictEqual(self.test2_expected, self.test2)

    def test_useful2(self):
        self.assertDictEqual(self.test3_expected, self.test3)


def main():
    unittest.main()

if __name__ == '__main__':
    main()