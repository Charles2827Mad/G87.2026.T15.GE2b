"""class for testing the register_order method"""
import unittest
from uc3m_consulting import EnterpriseManager, EnterpriseManagementException

class TestRegisterProject(unittest.TestCase):
    """class for testing the register_order method"""

    def test_TC1(self):
        pass

    def test_TC2(self):
        pass

    def test_TC3(self):
        pass

    def test_TC4(self):
        manager = EnterpriseManager()

        with self.assertRaises(EnterpriseManagementException):
            manager.register_document(
                "desktop/register_document/deletion/tc4-invalid_pdf.json"
            )

    def test_TC5(self):
        manager = EnterpriseManager()

        with self.assertRaises(EnterpriseManagementException):
            manager.register_document(
                "desktop/register_document/deletion/tc5-invalid_pdf.json"
            )

    def test_TC6( self ):
        manager = EnterpriseManager()

        with self.assertRaises(EnterpriseManagementException):
            manager.register_document(
                "desktop/register_document/deletion/tc6-invalid_pdf.json"
            )

    def test_TC7( self ):
        manager = EnterpriseManager()

        with self.assertRaises(EnterpriseManagementException):
            manager.register_document(
                "desktop/register_document/deletion/tc7-invalid_pdf.json"
            )

    def test_TC8( self ):
        manager = EnterpriseManager()

        with self.assertRaises(EnterpriseManagementException):
            manager.register_document(
                "desktop/register_document/deletion/tc8-invalid_pdf.json"
            )

    def test_TC9( self ):
        manager = EnterpriseManager()

        with self.assertRaises(EnterpriseManagementException):
            manager.register_document(
                "desktop/register_document/deletion/tc9-invalid_pdf.json"
            )

    def test_TC10( self ):
        manager = EnterpriseManager()

        with self.assertRaises(EnterpriseManagementException):
            manager.register_document(
                "desktop/register_document/deletion/tc10-invalid_pdf.json"
            )

    def test_TC11( self ):
        manager = EnterpriseManager()

        with self.assertRaises(EnterpriseManagementException):
            manager.register_document(
                "desktop/register_document/deletion/tc11-invalid_pdf.json"
            )

    def test_TC12(self):
        manager = EnterpriseManager()

        with self.assertRaises(EnterpriseManagementException):
            manager.register_document(
                "desktop/register_document/deletion/tc12-invalid_pdf.json"
            )

    def test_TC13(self):
        manager = EnterpriseManager()

        with self.assertRaises(EnterpriseManagementException):
            manager.register_document(
                "desktop/register_document/deletion/tc13-invalid_pdf.json"
            )

    def test_TC14(self):
        manager = EnterpriseManager()

        with self.assertRaises(EnterpriseManagementException):
            manager.register_document(
                "desktop/register_document/deletion/tc14-invalid_pdf.json"
            )

    def test_TC15(self):
        manager = EnterpriseManager()

        with self.assertRaises(EnterpriseManagementException):
            manager.register_document(
                "desktop/register_document/deletion/tc15-invalid_pdf.json"
            )

    def test_TC16(self):
        manager = EnterpriseManager()

        with self.assertRaises(EnterpriseManagementException):
            manager.register_document(
                "desktop/register_document/deletion/tc16-invalid_pdf.json"
            )

    def test_TC17(self):
        manager = EnterpriseManager()

        with self.assertRaises(EnterpriseManagementException):
            manager.register_document(
                "desktop/register_document/deletion/tc17-invalid_pdf.json"
            )

    def test_TC18(self):
        manager = EnterpriseManager()

        with self.assertRaises(EnterpriseManagementException):
            manager.register_document(
                "desktop/register_document/deletion/tc18-invalid_pdf.json"
            )

    def test_TC19(self):
        manager = EnterpriseManager()

        with self.assertRaises(EnterpriseManagementException):
            manager.register_document(
                "desktop/register_document/deletion/tc19-invalid_pdf.json"
            )

    def test_TC20(self):
        manager = EnterpriseManager()

        with self.assertRaises(EnterpriseManagementException):
            manager.register_document(
                "desktop/register_document/deletion/tc20-invalid_pdf.json"
            )

    def test_TC21(self):
        manager = EnterpriseManager()

        with self.assertRaises(EnterpriseManagementException):
            manager.register_document(
                "desktop/register_document/deletion/tc21-invalid_pdf.json"
            )

    def test_TC22(self):
        manager = EnterpriseManager()

        with self.assertRaises(EnterpriseManagementException):
            manager.register_document(
                "desktop/register_document/deletion/tc22-invalid_pdf.json"
            )


if __name__ == '__main__':
    unittest.main()
