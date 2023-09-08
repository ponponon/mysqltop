from typing import Optional
import click
import pymysql
from tabulate import tabulate
from mysqltop import VERSION


@click.group()
@click.version_option(version=VERSION)
def mysqltop_cli():
    pass


@mysqltop_cli.command()
@click.option('-h', '--host', default='127.0.0.1',         show_default=True, help='Database host')
@click.option('-u', '--user', help='Database username')
@click.option('-p', '--password', prompt='Enter password', hide_input=True, help='Database password')
@click.option('-P', '--port', type=int, default=3306,  show_default=True, help='Database port')
@click.option('-D', '--database',  help='Database name')
def shell(
    host: str,
    user: str,
    password: str,
    port: int = 3306,
    database: Optional[str] = None
):

    click.echo(
        f'Connecting to host: {host}, user: {user}, port: {port}')

    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=None  # 替换为你的数据库名称
    )

    try:
        # 创建游标对象
        cursor = conn.cursor()

        # 执行SQL查询以获取连接列表
        cursor.execute("SHOW PROCESSLIST")

        # 获取所有连接的详细信息
        connections = cursor.fetchall()

        # 构建表格数据
        table_data = []
        headers = ["连接ID", "用户", "主机", "数据库", "命令", "时间", "状态", "信息"]

        for connection in connections:
            connection_id, user, host, db, command, time, state, info = connection
            table_data.append([connection_id, user, host,
                              db, command, time, state, info])

        # 使用tabulate库将数据格式化为表格
        table = tabulate(table_data, headers, tablefmt="pretty")

        # 打印表格
        print(table)

    finally:
        # 关闭游标和数据库连接
        cursor.close()
        conn.close()


cli = click.CommandCollection(sources=[mysqltop_cli])


if __name__ == '__main__':
    cli()
