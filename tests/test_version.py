"""fundaily 目前是占位包，测试仅覆盖包可正常导入及版本号存在。"""

import fundaily


def test_import():
    """包应可正常导入。"""
    assert fundaily is not None


def test_version():
    """`__version__` 必须存在且为非空字符串。"""
    assert isinstance(fundaily.__version__, str)
    assert fundaily.__version__
