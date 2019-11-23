import requests

from unittest import main, TestCase
from unittest.mock import patch


class Test(TestCase):

    @patch('test_patch.requests')
    def test_download_google(mock_requests):
        result = requests.get('https://google.com')

        print(result)

        mock_requests.get.assert_called()


if __name__ == '__main__':
    main()
