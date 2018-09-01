
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
    expected = new_line
    curve_item = BasePlotCurveItem()
    curve_item.lineStyle = new_line
    assert expected == curve_item._pen.style()
    assert expected == curve_item.lineStyle


@pytest.mark.parametrize("new_width, expected", [
    (6, 6),
    ('10', 10),
    (4.3, 4),])
def test_base_plot_curve_item_line_width(new_width, expected):
    curve_item = BasePlotCurveItem()
    curve_item.lineWidth = new_width
    assert expected == curve_item._pen.width()
    assert expected == curve_item.lineWidth


@pytest.mark.parametrize("new_symbol, expected", [
    (None, None),
    ('o', 'o'),
    ('s', 's'),
    ('t', 't'),])
def test_base_plot_curve_item_symbol(new_symbol, expected):
    curve_item = BasePlotCurveItem()
    curve_item.symbol = new_symbol
    assert expected == curve_item.symbol


@pytest.mark.parametrize("new_size, expected", [
    (6, 6),
    ('10', 10),
    (4.3, 4),])
def test_base_plot_curve_item_symbol_size(new_size, expected):
    curve_item = BasePlotCurveItem()
    curve_item.symbolSize = new_size
    assert expected == curve_item.symbolSize


# --------------------
# NEGATIVE TEST CASES
# --------------------
@pytest.mark.parametrize(
    "new_color", [
        [0, 0, 0],
        (1, 1, 1),
        ]
    )
def test_base_plot_curve_item_color_invalid(caplog, new_color):
    curve_item = BasePlotCurveItem()
    expected = QColor(curve_item.color)
    curve_item.color = new_color

    assert expected == curve_item.color
    # Make sure logging capture the error, and have the correct error message
    for record in caplog.records:
        assert record.levelno == logging.ERROR


@pytest.mark.parametrize("new_line", ['NoLine', 7, ])
def test_base_plot_curve_item_line_style_invalid(caplog, new_line):
    curve_item = BasePlotCurveItem()
    expected_style = curve_item.lineStyle
    curve_item.lineStyle = new_line

    assert expected_style == curve_item.lineStyle
    # Make sure logging capture the error, and have the correct error message
    for record in caplog.records:
        assert record.levelno == logging.ERROR


@pytest.mark.parametrize("new_width", ['blah', (3, ), ])
def test_base_plot_curve_item_line_width_invalid(caplog, new_width):
    curve_item = BasePlotCurveItem()
    expected_width = curve_item.lineWidth
    curve_item.lineWidth = new_width
    assert expected_width == curve_item.lineWidth
    # Make sure logging capture the error, and have the correct error message
    for record in caplog.records:
        assert record.levelno == logging.ERROR


@pytest.mark.parametrize("new_symbol", [1, 'b', (2, )])
def test_base_plot_curve_item_symbol_invalid(caplog, new_symbol):
    curve_item = BasePlotCurveItem()
    expected = curve_item.symbol
    curve_item.symbol = new_symbol
    assert expected == curve_item.symbol
    # Make sure logging capture the error, and have the correct error message
    for record in caplog.records:
        assert record.levelno == logging.ERROR


@pytest.mark.parametrize("new_size", ['blah', (3, ), ])
def test_base_plot_curve_item_symbol_size_invalid(caplog, new_size):
    curve_item = BasePlotCurveItem()
    expected = curve_item.symbolSize
    curve_item.symbolSize = new_size
    assert expected == curve_item.symbolSize
    # Make sure logging capture the error, and have the correct error message
    for record in caplog.records:
        assert record.levelno == logging.ERROR


