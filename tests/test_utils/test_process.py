from __future__ import absolute_import
from unittest import TestCase

import pandas as pd
from pandas.testing import assert_frame_equal
from utils.proccess import populate_data


class TestUtils(TestCase):

    def setup(self):
        pass

    def test_populate_data(self):
        data1 = []
        data2 = []
        response = populate_data(data1, data2)
        expected = pd.DataFrame(columns=['SL No.', 'Title', 'Price', 'Title', 'Price'])
        assert_frame_equal(response, expected)
