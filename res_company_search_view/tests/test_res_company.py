from odoo.addons.base.tests.common import BaseCommon


class TestResCompany(BaseCommon):
    def setUp(self):
        super().setUp()
        # Create a test company for use in test cases
        self.company = self.env["res.company"].create(
            {
                "name": "Test Company",
                "country_id": self.env.ref("base.us").id,
                "street": "123 Test Street",
                "street2": "Suite 456",
                "zip": "12345",
                "city": "Test City",
                "state_id": self.env.ref("base.state_us_1").id,
            }
        )

    def test_create_company_with_address(self):
        """Test creation of a company with address details."""
        self.assertEqual(
            self.company.street, "123 Test Street", "Street value is incorrect"
        )
        self.assertEqual(
            self.company.street2, "Suite 456", "Street2 value is incorrect"
        )
        self.assertEqual(self.company.zip, "12345", "ZIP code value is incorrect")
        self.assertEqual(self.company.city, "Test City", "City value is incorrect")
        self.assertEqual(
            self.company.state_id,
            self.env.ref("base.state_us_1"),
            "State value is incorrect",
        )
        self.assertEqual(
            self.company.country_id,
            self.env.ref("base.us"),
            "Country value is incorrect",
        )

    def test_update_company_address(self):
        """Test updating the address details of a company."""
        self.company.write(
            {
                "street": "789 New Street",
                "street2": "Apt 101",
                "zip": "67890",
                "city": "New City",
                "state_id": self.env.ref("base.state_us_2").id,
                "country_id": self.env.ref("base.ca").id,
            }
        )
        self.assertEqual(
            self.company.street,
            "789 New Street",
            "Street value did not update correctly",
        )
        self.assertEqual(
            self.company.street2, "Apt 101", "Street2 value did not update correctly"
        )
        self.assertEqual(
            self.company.zip, "67890", "ZIP code value did not update correctly"
        )
        self.assertEqual(
            self.company.city, "New City", "City value did not update correctly"
        )
        self.assertEqual(
            self.company.state_id,
            self.env.ref("base.state_us_2"),
            "State value did not update correctly",
        )
        self.assertEqual(
            self.company.country_id,
            self.env.ref("base.ca"),
            "Country value did not update correctly",
        )

    def test_create_company_with_partial_address(self):
        """Test creation of a company with partial address details."""
        partial_company = self.env["res.company"].create(
            {
                "name": "Partial Address Company",
                "street": "456 Partial Street",
                "zip": "54321",
                "city": "Partial City",
            }
        )
        self.assertEqual(
            partial_company.street,
            "456 Partial Street",
            "Partial street value is incorrect",
        )
        self.assertEqual(
            partial_company.zip, "54321", "Partial ZIP code value is incorrect"
        )
        self.assertEqual(
            partial_company.city, "Partial City", "Partial city value is incorrect"
        )
        self.assertFalse(
            partial_company.country_id, "Country should not be set for partial address"
        )
        self.assertFalse(
            partial_company.state_id, "State should not be set for partial address"
        )
