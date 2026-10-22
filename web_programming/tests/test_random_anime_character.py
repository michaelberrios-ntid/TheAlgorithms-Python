from unittest.mock import Mock, patch, ANY

import pytest
import httpx

import web_programming.random_anime_character as sut

TEST_IMAGE_URL = "www.image.com"
TEST_IMAGE_TITLE = "Monkey D. Luffy"
TEST_IMAGE_DESCRIPTION = "A small pirate in a straw hat with big dreams"

@patch(sut.httpx.get)
@patch(sut.file.write)
def test_save_image(file_write, httpx_get):
    fake_image = Mock()
    fake_image.content = TEST_IMAGE_DESCRIPTION
    httpx_get.return_value = fake_image

    sut.save_image(TEST_IMAGE_URL, TEST_IMAGE_TITLE)
    httpx_get.assert_called_once_with(TEST_IMAGE_URL, headers = ANY, timeout = ANY)
    file_write.assert_called_once_with(TEST_IMAGE_DESCRIPTION)

