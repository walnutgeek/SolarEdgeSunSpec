# SolarEdge's SunSpec

Reading and formating registers from SE inverter via modbus. Registers definitions
stored in [CSV](se_ss/registers.csv) derived from
[SolarEdge technical notes](https://www.solaredge.com/sites/default/files/sunspec-implementation-technical-note.pdf)


For script to work, Modbus TCP need to be enabled in invertor. Refer 
page 14 of technical notes for instructions to enable.


## Usage
```
$ python -m se_ss.cli --help 
Usage: cli.py [OPTIONS] [[C_SunSpec_ID|C_SunSpec_DID|C_SunSpec_Length|C_Manufa
              cturer|C_Model|C_Version|C_SerialNumber|C_DeviceAddress|C_SunSpe
              c_DID2|C_SunSpec_Length2|I_AC_Current|I_AC_CurrentA|I_AC_Current
              B|I_AC_CurrentC|I_AC_Current_SF|I_AC_VoltageAB|I_AC_VoltageBC|I_
              AC_VoltageCA|I_AC_VoltageAN|I_AC_VoltageBN|I_AC_VoltageCN|I_AC_V
              oltage_SF|I_AC_Power|I_AC_Power_SF|I_AC_Frequency|I_AC_Frequency
              _SF|I_AC_VA|I_AC_VA_SF|I_AC_VAR|I_AC_VAR_SF|I_AC_PF|I_AC_PF_SF|I
              _AC_Energy_WH|I_AC_Energy_WH_SF|I_DC_Current|I_DC_Current_SF|I_D
              C_Voltage|I_DC_Voltage_SF|I_DC_Power|I_DC_Power_SF|I_Temp_Sink|I
              _Temp_SF|I_Status|I_Status_Vendor]]...

Options:
  --ip TEXT           IP address of Modbus TCP.
  --port INTEGER      port number
  --out [json|human]  json or human
  --help              Show this message and exit.
$  

```

Something like:
```
$ python -m se_ss.cli --ip 192.168.1.17 C_SunSpec_DID2 I_AC_Current I_AC_Current_SF I_AC_VoltageAB I_AC_Power I_AC_Power_SF I_DC_Power I_DC_Power_SF
C_SunSpec_DID2  = 102    # 101 = single phase; 102 = split phase; 103 = three phase
I_AC_Current    = 0      # AC Total Current value
I_AC_Current_SF = -2     # AC Current scale factor
I_AC_VoltageAB  = 2454   # AC Voltage Phase AB value
I_AC_Power      = 0      # AC Power value
I_AC_Power_SF   = 0      # AC Power scale factor
I_DC_Power      = 0      # DC Power value
I_DC_Power_SF   = 0      # Scale factor
$
```