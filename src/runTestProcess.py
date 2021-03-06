import os
from multiprocessing import Pool


class RunTestProcess:
    def __init__(self, p1, p2, p3, p4):
        self.test_processes = (p1, p2, p3, p4)
        self.pool = Pool(processes=4)
        pass

    @staticmethod
    def run_tests(process):
        os.system('python {}'.format(process))
    def test_pool(self) -> object:
        self.pool.map(self.run_tests, self.test_processes)

    @staticmethod
    def main():
        this_process = RunTestProcess('src/tests/calculatorTest.py', 'src/tests/generalStatisticsTest.py','src/tests/populationStatisticsTest.py',
                                      'src/tests/sampleStatisticsTest.py')
        this_process.test_pool()