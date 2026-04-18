"""class for testing the register_order method"""
import unittest
from uc3m_consulting import EnterpriseManager, EnterpriseManagementException

class TestRegisterProject(unittest.TestCase):
    """class for testing the register_order method"""
    def test_TC4( self ):
        manager = EnterpriseManager()

        with self.assertRaises(EnterpriseManagementException):
            manager.register_document(
                "desktop/register_document/deletion/tc5-invalid_pdf.json"
            )


if __name__ == '__main__':
    unittest.main()
