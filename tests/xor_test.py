import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def xor_test(dut):
    a = (0, 0, 1, 1)
    b = (0, 1, 0, 1)
    y = (0, 1, 1, 0)

    for i in range(4):
        dut.a.value = a[i]
        dut.b.value = b[i]
        await Timer(1, 'ns')
        actual = int(dut.y.value)
        expected = y[i]
        print(f"Test {i}: a={a[i]} b={b[i]} → y={actual} (expected {expected})")
        assert actual == expected, f"Error at iteration {i}: got {actual}, expected {expected}"
