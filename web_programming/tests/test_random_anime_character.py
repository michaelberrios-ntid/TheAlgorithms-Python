import os.path
from unittest.mock import Mock, patch, ANY, mock_open

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
@patch("web_programming.random_anime_character.httpx.get")
@patch("builtins.open", new_callable=mock_open)
def test_save_image(file_open, httpx_get):
    fake_image = Mock()
    fake_image.content = TEST_IMAGE_DESCRIPTION
    httpx_get.return_value = fake_image




    sut.save_image(TEST_IMAGE_URL, TEST_IMAGE_TITLE)
    httpx_get.assert_called_once_with(TEST_IMAGE_URL, headers = ANY, timeout = ANY)

    file_open.assert_called_once_with(TEST_IMAGE_TITLE, "wb")
    file_open().write.assert_called_once_with(TEST_IMAGE_DESCRIPTION)


"""
    Soup mock side effects. Used to determine behavior from soup.find
"""

def soup_side_effects(*args, **kwargs):
    if "attrs" in kwargs:
        if kwargs.get("attrs")["property"]=="og:title":
            title_tag = Mock()
            title_tag.attrs = {"content": TEST_IMAGE_TITLE}
            return title_tag
        if kwargs.get("attrs")["property"] == "og:image":
            image_tag = Mock()
            image_tag.attrs = {"content": TEST_IMAGE_URL}
            return image_tag
        return None
    elif kwargs.get("id") == "description":
        description_tag = Mock()
        description_tag.get_text.return_value = TEST_IMAGE_DESCRIPTION
        return description_tag
    else:
        return Mock()

"""
Tests random_anime_character()
"""

@patch("web_programming.random_anime_character.save_image")
@patch("web_programming.random_anime_character.httpx.get")
@patch("web_programming.random_anime_character.BeautifulSoup")
@patch("web_programming.random_anime_character.os.path.splitext")
def test_random_anime_character(os_path_splittext, beautiful_soup,httpx_get,save_image):
    fake_soup = Mock()

    fake_soup.find.side_effect = soup_side_effects

    beautiful_soup.return_value = fake_soup

    os_path_splittext.return_value = 'X', ".png"

    title, description, image_title = sut.random_anime_character()

    beautiful_soup.assert_called_once()
    httpx_get.assert_called_once()
    assert title == TEST_IMAGE_TITLE
    assert description == TEST_IMAGE_DESCRIPTION
    assert image_title == TEST_IMAGE_FILE_TITLE

