import unittest
from populationStatistics import populationStatistics


class PopulationStatisticsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.p_stats = populationStatistics()

    def test_something(self):
        self.assertIsInstance(self.p_stats, populationStatistics)


if __name__ == '__main__':
    unittest.main()