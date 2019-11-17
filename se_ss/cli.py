import json
from time import sleep
from typing import List

import click
from pymodbus.client.sync import ModbusTcpClient

import se_ss

NAME_CHOICES = list(se_ss.entries_by_name.keys())


def read_regs(ip, port=502):
    for i in range(3):
        if i != 0:
            sleep(1)
        c = ModbusTcpClient(ip, port)
        count = se_ss.entries[-1].end_addr - se_ss.start_addr

        r = c.read_holding_registers(se_ss.start_addr - 1, count, unit=1)
        # dont know why I have to `start_addr-1` but otherwise it off by 1

        from pymodbus.exceptions import ModbusIOException

        if not isinstance(r, ModbusIOException):
            return r.encode()[1:]  # remove size in begining of buff
    raise r


@click.command()
@click.option("--ip", prompt="IP", help="IP address of Modbus TCP.")
@click.option("--port", default=502, help="port number", type=int)
@click.option(
    "--out",
    default="human",
    help="json or human",
    type=click.Choice(["json", "human"], case_sensitive=False),
)
@click.argument(
    "columns", nargs=-1, type=click.Choice(NAME_CHOICES, case_sensitive=True)
)
def main(ip: str, port: int = 502, out="human", columns: List[str] = []):
    if not columns:
        columns = NAME_CHOICES
    # from se_ss.tests import sample; r = sample('at_night.bin')
    r = read_regs(ip, port)
    d = {k: se_ss.entries_by_name[k].extract(r) for k in columns}
    if out == "json":
        print(json.dumps(d))
    else:
        d = {k: str(v) for k, v in d.items()}
        max_k = max(map(len, d.keys()))
        max_v = max(map(len, d.values()))

        def pad(v, l):
            return f'{v}{" " * (l-len(v))}'

        for k, v in d.items():
            e = se_ss.entries_by_name[k]
            print(f"{pad(k,max_k)} = {pad(v,max_v)}   # {e.description}")


if __name__ == "__main__":
    main()
