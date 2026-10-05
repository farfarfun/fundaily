# Changelog

本项目的版本记录按版本倒序排列，每个版本分「新增」「修复」「变更」「废弃」四类。

## [未发布]

### 新增

- `pyproject.toml` 补 `[project.urls]`（PyPI 主页、仓库、组织主页）与 `[tool.ruff]` / `[tool.ruff.lint]` / `[tool.pytest.ini_options]` 配置，dev 依赖组加入 `ruff`。
- 测试补版本漂移拦截用例：断言 `fundaily.__version__` 与 `pyproject.toml` 的 `[project].version` 一致、且未回退到占位值。

### 修复

- sdist 显式排除本地生成的 `uv.lock`，避免其进入发布源码包。

### 变更

- `fundaily.__version__` 不再硬编码，改为通过 `importlib.metadata` 读取发行元数据，使 `pyproject.toml` 的 `[project].version` 成为唯一版本来源，避免两处漂移。
- `[project].description` 由占位的 `fundaily` 改为据实描述（SPEC §11 禁止模板套话）。
- 清理 `.gitignore` 里残留的其他仓库规则（`funwork.egg-info/*` 等），`dist/`、`build/`、`*.egg-info/` 已由上方通用规则覆盖。

### 废弃

- 无

## [0.0.1]

### 新增

- 初始占位发布（[PyPI 0.0.1](https://pypi.org/project/fundaily/0.0.1/)），仅用于保留 `fundaily` 包名，尚无实际功能代码。

### 修复

- 无

### 变更

- 无

### 废弃

- 无
