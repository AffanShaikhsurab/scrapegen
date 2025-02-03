import pytest
from bs4 import BeautifulSoup
from unittest.mock import Mock

@pytest.fixture
def sample_html_content():
    return """
    <html>
        <body>
            <h1>Company Name</h1>
            <p>Company Description</p>
            <a href="/about">About Us</a>
            <a href="https://example.com/contact">Contact</a>
            <h2>CEO: John Doe</h2>
            <p>Funding: $10M</p>
        </body>
    </html>
    """

@pytest.fixture
def mock_response(sample_html_content):
    mock = Mock()
    mock.text = sample_html_content
    mock.raise_for_status = Mock()
    return mock