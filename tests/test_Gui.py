import pytest

from src.Gui import Gui


@pytest.fixture
def gui():
    gui_instance = Gui()
    yield gui_instance
    gui_instance.window.destroy()


@pytest.mark.Gui
def test_on_button_click(gui):
    gui.on_button_click("/")
    gui.on_button_click(5)
    gui.on_button_click("*")
    gui.on_button_click("+")
    gui.on_button_click(5)
    assert gui.entered_string.get() == "5+5"


@pytest.mark.Gui
def test_clear_button(gui):
    gui.entered_string.set("123")
    gui.clear_button()
    assert gui.entered_string.get() == ""


@pytest.mark.Gui
def test_memory_add(gui):
    gui.entered_string.set("10")
    gui.memory_add()
    assert gui.memory == 10


@pytest.mark.Gui
def test_memory_clear(gui):
    gui.memory = 10
    gui.memory_clear()
    assert gui.memory == 0


@pytest.mark.Gui
def test_memory_recall(gui):
    gui.memory = 15
    gui.memory_recall()
    assert gui.entered_string.get() == "15"


@pytest.mark.Gui
def test_memory_store(gui):
    gui.entered_string.set("7")
    gui.memory_store()
    assert gui.memory == 7


@pytest.mark.Gui
def test_negate(gui):
    gui.entered_string.set("10")
    gui.negate()
    assert gui.entered_string.get() == "-10.0"


@pytest.mark.Gui
def test_on_equal_sign_click(gui):
    gui.entered_string.set("2+3")
    gui.on_equal_sign_click()
    assert gui.entered_string.get() == "5"
