
import pytest
import logging

from ...PyQt.QtGui import QColor
from ...utilities.colors import svg_color_from_hex
from ...widgets.baseplot import BasePlotCurveItem, BasePlot


# --------------------
# POSITIVE TEST CASES
# --------------------

@pytest.mark.parametrize(
    "new_color", [
        "#00FF00",
        "#0000FF",
        QColor("#FF0000"),
        'blahh',
        'white',
        200,
        34.98,
        ]
    )
def test_base_plot_curve_item_color(new_color):
    expected = QColor(new_color)
    expected_string = svg_color_from_hex(
                                    expected.name(), hex_on_fail=True)

    curve_item = BasePlotCurveItem()
    curve_item.color = new_color

    assert expected_string == curve_item.color_string
    assert expected == curve_item.color


@pytest.mark.parametrize("new_line", [0, 1, 5, ])
def test_base_plot_curve_item_line_style(new_line):
    """
    Test lineStyle setting for the item.

    Expectations:
    The item attribute is set appropriately


    Parameters
    ----------
    new_line : int
        new attribute value

    """
    expected = new_line
    curve_item = BasePlotCurveItem()
    curve_item.lineStyle = new_line
    assert expected == curve_item._pen.style()
    assert expected == curve_item.lineStyle


@pytest.mark.parametrize("new_width, expected", [
    (6, 6),
    ('10', 10),
    (4.3, 4), ])
def test_base_plot_curve_item_line_width(new_width, expected):
    """
    Test lineWidth setting for the item.

    Expectations:
    The item attribute is set appropriately


    Parameters
    ----------
    new_width : int, float or string
        new attribute value
    expected : int
        expected value for the item attribute

    """
    curve_item = BasePlotCurveItem()
    curve_item.lineWidth = new_width
    assert expected == curve_item._pen.width()
    assert expected == curve_item.lineWidth


@pytest.mark.parametrize("new_symbol, expected", [
    (None, None),
    ('o', 'o'),
    ('s', 's'),
    ('t', 't'), ])
def test_base_plot_curve_item_symbol(new_symbol, expected):
    """
    Test symbol setting for the item.

    Expectations:
    The item attribute is set appropriately


    Parameters
    ----------
    new_symbol : str
        new attribute value
    expected : str
        expected value for the item attribute

    """
    curve_item = BasePlotCurveItem()
    curve_item.symbol = new_symbol
    assert expected == curve_item.symbol


@pytest.mark.parametrize("new_size, expected", [
    (6, 6),
    ('10', 10),
    (4.3, 4), ])
def test_base_plot_curve_item_symbol_size(new_size, expected):
    """
    Test symbolSize setting for the item.

    Expectations:
    The item attribute is set appropriately


    Parameters
    ----------
    new_size : int, float or str
        new attribute value
    expected : int
        expected value for the item attribute

    """
    curve_item = BasePlotCurveItem()
    curve_item.symbolSize = new_size
    assert expected == curve_item.symbolSize


@pytest.mark.parametrize("kws, expected", [
    (dict(),
     {'lineStyle': 1, 'lineWidth': 1, 'name': None, 'color': 'white',
      'symbol': None, 'symbolSize': 10}),
    ({'lineStyle': 4, 'lineWidth': 3, 'name': 'blah', 'color': 'blue',
      'symbol': '+', 'symbolSize': 50},
     {'lineStyle': 4, 'lineWidth': 3, 'name': 'blah', 'color': 'blue',
      'symbol': '+', 'symbolSize': 50})])
def test_base_plot_curve_constructor(kws, expected):
    """
    Test the construction of the item.

    Expectations:
    The item is constructed with the correct default values
    The item is constructed with the correct input argument values

    Parameters
    ----------
    kws : dictionary
        keyword arguments for the constructor
    expected : dictionary
        expected values for the item attributes

    """
    curve_item = BasePlotCurveItem(**kws)
    assert curve_item.lineStyle == expected['lineStyle']
    assert curve_item.lineWidth == expected['lineWidth']
    assert curve_item.name() == expected['name']
    assert curve_item.color_string == expected['color']
    assert curve_item.symbol == expected['symbol']
    assert curve_item.symbolSize == expected['symbolSize']


# --------------------
# NEGATIVE TEST CASES
# --------------------
@pytest.mark.parametrize("new_color", [
    [0, 0, 0],
    (1, 1, 1), ])
def test_base_plot_curve_item_color_invalid(caplog, new_color):
    """
    Test wrong color setting for the item.

    Expectations:
    The item attribute is not set and error message in recorded


    Parameters
    ----------
    caplog : fixture
        To capture the log messages
    new_color : list or tuple
        new attribute value

    """
    curve_item = BasePlotCurveItem()
    expected = QColor(curve_item.color)
    curve_item.color = new_color

    assert expected == curve_item.color
    # Make sure logging capture the error, and have the correct error message
    for record in caplog.records:
        assert record.levelno == logging.ERROR


@pytest.mark.parametrize("new_line", ['NoLine', 7, ])
def test_base_plot_curve_item_line_style_invalid(caplog, new_line):
    """
    Test wrong lineStyle setting for the item.

    Expectations:
    The item attribute is not set and error message in recorded


    Parameters
    ----------
    caplog : fixture
        To capture the log messages
    new_line : str or int
        new attribute value

    """
    curve_item = BasePlotCurveItem()
    expected_style = curve_item.lineStyle
    curve_item.lineStyle = new_line

    assert expected_style == curve_item.lineStyle
    # Make sure logging capture the error, and have the correct error message
    for record in caplog.records:
        assert record.levelno == logging.ERROR


@pytest.mark.parametrize("new_width", ['blah', (3, ), ])
def test_base_plot_curve_item_line_width_invalid(caplog, new_width):
    """
    Test wrong lineWidth setting for the item.

    Expectations:
    The item attribute is not set and error message in recorded


    Parameters
    ----------
    caplog : fixture
        To capture the log messages
    new_width : str or tuple
        new attribute value

    """
    curve_item = BasePlotCurveItem()
    expected_width = curve_item.lineWidth
    curve_item.lineWidth = new_width
    assert expected_width == curve_item.lineWidth
    # Make sure logging capture the error, and have the correct error message
    for record in caplog.records:
        assert record.levelno == logging.ERROR


@pytest.mark.parametrize("new_symbol", [1, 'b', (2, )])
def test_base_plot_curve_item_symbol_invalid(caplog, new_symbol):
    """
    Test wrong symbol setting for the item.

    Expectations:
    The item attribute is not set and error message in recorded


    Parameters
    ----------
    caplog : fixture
        To capture the log messages
    new_symbol : int, str or tuplse
        new attribute value

    """
    curve_item = BasePlotCurveItem()
    expected = curve_item.symbol
    curve_item.symbol = new_symbol
    assert expected == curve_item.symbol
    # Make sure logging capture the error, and have the correct error message
    for record in caplog.records:
        assert record.levelno == logging.ERROR


@pytest.mark.parametrize("new_size", ['blah', (3, ), ])
def test_base_plot_curve_item_symbol_size_invalid(caplog, new_size):
    """
    Test wrong symbolSize setting for the item.

    Expectations:
    The item attribute is not set and error message in recorded


    Parameters
    ----------
    caplog : fixture
        To capture the log messages
    new_size : str or tuple
        new attribute value

    """
    curve_item = BasePlotCurveItem()
    expected = curve_item.symbolSize
    curve_item.symbolSize = new_size
    assert expected == curve_item.symbolSize
    # Make sure logging capture the error, and have the correct error message
    for record in caplog.records:
        assert record.levelno == logging.ERROR
