from testlab_easy import Testlab

tl = Testlab()
project = tl.open("test.lms")

signals = project.section("TimeData").list()

avg = project.processing.average(signals)

project.results.write_block("AVG", avg)

project.export.to_csv("AVG", "avg.csv")
