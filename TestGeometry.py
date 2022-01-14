import unittest
import p4geom

class TestMyStuff(unittest.TestCase):

    def test_squarePerim(self):
        self.assertEqual("20.0000", format(p4geom.squarePerim(5),".4f"))

    def test_squareArea(self):
        self.assertEqual("25.0000", format(p4geom.squareArea(5),".4f"))

    def test_CubeVolume(self):
        self.assertEqual("125.0000", format(p4geom.cubeVolume(5),".4f"))

    def test_cubeSurfArea(self):
        self.assertEqual("150.0000", format(p4geom.cubeSurfArea(5),".4f"))

    def test_circleCircum(self):
        self.assertEqual("31.4159", format(p4geom.circleCircum(5),".4f"))

    def test_circleArea(self):
        self.assertEqual("78.5398", format(p4geom.circleArea(5), ".4f"))

    def test_sphereVolume(self): #this isn't rounded correctly. It should be 523.5987
        self.assertEqual("523.5988", format(p4geom.sphereVolume(5), ".4f"))
        
    def test_sphereSurfArea(self):
        self.assertEqual("314.1593", format(p4geom.sphereSurfArea(5), ".4f"))
    
def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMyStuff)
    unittest.TextTestRunner(verbosity = 2).run(suite)

main()
