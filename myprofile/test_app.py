import unittest
from app import app

class TestMyProfileApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_profile_page_loads(self):
        """Test that the profile page loads successfully"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John Doe', response.data)
        self.assertIn(b'Software Developer', response.data)

    def test_contact_information_present(self):
        """Test that contact information is displayed"""
        response = self.app.get('/')
        self.assertIn(b'john.doe@example.com', response.data)
        self.assertIn(b'+1 (555) 123-4567', response.data)
        self.assertIn(b'San Francisco, CA', response.data)

    def test_skills_section_present(self):
        """Test that skills are displayed"""
        response = self.app.get('/')
        self.assertIn(b'Python', response.data)
        self.assertIn(b'JavaScript', response.data)
        self.assertIn(b'React', response.data)

    def test_experience_section_present(self):
        """Test that experience information is displayed"""
        response = self.app.get('/')
        self.assertIn(b'Tech Corp', response.data)
        self.assertIn(b'Senior Developer', response.data)
        self.assertIn(b'StartupXYZ', response.data)

    def test_accessibility_attributes(self):
        """Test that proper accessibility attributes are present"""
        response = self.app.get('/')
        html_content = response.data.decode('utf-8')
        
        # Check for semantic HTML elements
        self.assertIn('role="banner"', html_content)
        self.assertIn('role="main"', html_content)
        self.assertIn('role="contentinfo"', html_content)
        
        # Check for proper heading structure
        self.assertIn('<h1>', html_content)
        self.assertIn('<h2 id="contact-heading">', html_content)
        self.assertIn('<h3>', html_content)
        
        # Check for aria-labelledby attributes
        self.assertIn('aria-labelledby="contact-heading"', html_content)
        self.assertIn('aria-labelledby="about-heading"', html_content)
        self.assertIn('aria-labelledby="skills-heading"', html_content)
        self.assertIn('aria-labelledby="experience-heading"', html_content)

if __name__ == '__main__':
    unittest.main()