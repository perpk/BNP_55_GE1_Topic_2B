import unittest

from sample.has_protein_weight_eq import has_protein_weight_eq

class HasProteinWeightEq(unittest.TestCase):
    def testHasProteinWithWeight(self):
        data = {'IFNAR2':[1, 10]}
        res = has_protein_weight_eq(data, 10)
        assert any(res) == True

    def testHasNoProteinWithWeight(self):
        data = {'INSULIN': [11, 12]}
        res = has_protein_weight_eq(data, 9)
        assert any(res) == False

    def testWeightsAreStrings(self):
        data = {'HEMOGLOBIN': ['10', '24']}
        res = has_protein_weight_eq(data, 24)
        assert any(res) == True

    def testWeightsAreDoublePrecision(self):
        data = {'CIROP': [9.99999, 10.0001]}
        res = has_protein_weight_eq(data, 10)
        assert any(res) == False