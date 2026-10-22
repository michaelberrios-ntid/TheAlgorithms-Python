import os.path
from unittest.mock import Mock, patch, ANY

import pytest
import httpx
from bs4 import BeautifulSoup

import web_programming.random_anime_character as sut

TEST_IMAGE_URL = "www.image.com"
TEST_IMAGE_TITLE = "Monkey D Luffy"
TEST_IMAGE_FILE_TITLE = "Monkey_D_Luffy.png"
TEST_IMAGE_DESCRIPTION = "A small pirate in a straw hat with big dreams"

"""
    Tests the save_image() function on correct behavior
"""
@patch(sut.httpx.get)
@patch(sut.file.write)
def test_save_image(file_write, httpx_get):
    fake_image = Mock()
    fake_image.content = TEST_IMAGE_DESCRIPTION
    httpx_get.return_value = fake_image

    sut.save_image(TEST_IMAGE_URL, TEST_IMAGE_TITLE)
    httpx_get.assert_called_once_with(TEST_IMAGE_URL, headers = ANY, timeout = ANY)
    file_write.assert_called_once_with(TEST_IMAGE_DESCRIPTION)


"""
    Behavior of mocked soup object
"""
def find_side_effects(args):
    if args[1].get("property") == "og:title":
        return TEST_IMAGE_TITLE
    elif args[1].get("property") == "og:image":
        return TEST_IMAGE_URL
    elif args[1] == "description":
        return TEST_IMAGE_DESCRIPTION
    return None


"""
Tests random_anime_character()
"""

@patch(sut.httpx.get)
@patch(sut.BeautifulSoup)
@patch(sut.os.path.splitext)
def test_random_anime_character(os_path_splittext, beautiful_soup, httpx_get):
    fake_soup = Mock()
    fake_soup.find.side_effect = find_side_effects

    beautiful_soup.return_value = fake_soup

    httpx_get.assert_called_once()
    beautiful_soup.assert_called_once()

    os_path_splittext.return_value = 'X', ".png"

    title, description, image_title = sut.random_anime_character()

    assert title == TEST_IMAGE_TITLE
    assert description == TEST_IMAGE_DESCRIPTION
    assert image_title == TEST_IMAGE_FILE_TITLE

