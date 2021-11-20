from Tests.testCRUD import testAdaugaCheltuiala, testModificaCheltuiala
from Tests.testDomain import testCheltuiala
from Tests.testFunctionalitati import testSumaMaximaTip, testCrestereSuma, testSumaLunara, testCorectitudineData


def runAllTest():
    testCheltuiala()
    testAdaugaCheltuiala()
    testSumaMaximaTip()
    testCrestereSuma()
    testModificaCheltuiala()
    testSumaLunara()
    testCorectitudineData()
