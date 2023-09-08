# mysqltop

<p align="center">
    <!-- <a href="https://github.com/ponponon/mysqltop/actions/workflows/tests.yml" target="_blank">
        <img src="https://github.com/ponponon/mysqltop/actions/workflows/tests.yml/badge.svg" alt="Tests coverage"/>
    </a>
    <a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/lancetnik/mysqltop" target="_blank">
        <img src="https://coverage-badge.samuelcolvin.workers.dev/lancetnik/mysqltop.svg" alt="Coverage">
    </a> -->
    <a href="https://pypi.org/project/mysqltop" target="_blank">
        <img src="https://img.shields.io/pypi/v/mysqltop?label=pypi%20package" alt="Package version">
    </a>
    <a href="https://pepy.tech/project/mysqltop" target="_blank">
        <img src="https://static.pepy.tech/personalized-badge/mysqltop?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads" alt="downloads"/>
    </a>
    <br/>
    <a href="https://pypi.org/project/mysqltop" target="_blank">
        <img src="https://img.shields.io/pypi/pyversions/mysqltop.svg" alt="Supported Python versions">
    </a>
    <a href="https://github.com/ponponon/mysqltop/blob/master/LICENSE" target="_blank">
        <img alt="GitHub" src="https://img.shields.io/github/license/ponponon/mysqltop?color=%23007ec6">
    </a>
</p>

[简体中文](./README.zh-CN.md) | [English](./README.md)

## 介绍

这个工具是 docker 官方命令行工具的补充版本，可以人类友好的方式输出容器信息，增加可读性

⭐️ 🌟 ✨ ⚡️ ☄️ 💥

## 安装

软件包已经上传到 PyPI: [mysqltop](https://pypi.org/project/mysqltop/)

可以直接使用 pip 安装:

```shell
pip install mysqltop
```

## 依赖

- Python : 3.8 及以上

## 文档

📄 暂无

## 示例

### 查看容器运行状态

可以在终端输入: `mysqltop shell -h 192.168.31.245 -uroot -p123456`

输出如下：

```shell
Connecting to host: 192.168.31.245, user: root, port: 3306
+--------+-----------------+----------------------+--------+--------+-------+------------------------+------------------+
| 连接ID |      用户       |         主机         | 数据库 |  命令  | 时间  |          状态          |       信息       |
+--------+-----------------+----------------------+--------+--------+-------+------------------------+------------------+
|   5    | event_scheduler |      localhost       |        | Daemon | 16047 | Waiting on empty queue |                  |
|   10   |      root       | 192.168.31.245:40022 |        | Sleep  | 3948  |                        |                  |
|   73   |      root       | 192.168.31.245:57088 |        | Query  |   0   |          init          | SHOW PROCESSLIST |
+--------+-----------------+----------------------+--------+--------+-------+------------------------+------------------+
```
