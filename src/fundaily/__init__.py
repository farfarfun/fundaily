"""fundaily：占位包，当前仅暴露 ``__version__``。

版本号的唯一来源是 ``pyproject.toml`` 的 ``[project].version``，这里通过发行
元数据读取，避免源码与打包声明两处硬编码产生漂移。
"""

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _metadata_version

__all__ = ["__version__"]

try:
    __version__: str = _metadata_version("fundaily")
except PackageNotFoundError:  # 直接从源码树导入、包未安装时
    __version__ = "0.0.0+unknown"
