
# PyModbus套件TCP範例程式碼
# 可搭配Modbus Slave Simulator來測試
from pymodbus.client import ModbusTcpClient
from pymodbus.transaction import ModbusSocketFramer

# 連線設定
client = ModbusTcpClient(
    host="192.168.0.195",
    port=502,
    framer=ModbusSocketFramer,
)

# 開始連線
connection = client.connect()

if  connection:

    print("connect successs!")

    try:

        # 讀取暫存器(Registers)資料
        # 此處範例為讀取40001-40005地址暫存器值
        res = client.read_holding_registers(
            address=0,  # 起始地址
            count=5,  # 讀取地址數
            slave=1,
        )
        print(res.registers)

    except:
        
        print("Modbus未成功連線!")

    finally:
        client.close()