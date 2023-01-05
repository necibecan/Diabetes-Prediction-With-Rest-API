import unittest
import requests

class PredictionTest(unittest.TestCase):
    URL = "http://127.0.0.1:5000/Predict"
    testData = {
        "pregnanciesNo" : 6,
        "bldGlucose" : 148,
        "bldPressure" : 72,
        "sknThk" : 35,
        "insulin" : 0,
        "bmi" : 33.6,
        "dmPedigreeFunc" : 0.627,
        "age" : 50
    }

    def test_prediction(self):
        resp = requests.post(self.URL, self.testData)
        self.assertEqual(resp.status_code, 200) #testing status code
        self.assertGreater(resp.text.find("[1]"), 0) #testing result via our datasets' first row, result must be 1
        print("Prediction test successfully done.")

if __name__ == "__main__":
    tester = PredictionTest()
    tester.test_prediction()