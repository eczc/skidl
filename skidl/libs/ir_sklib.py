from skidl import Pin, Part, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

ir = SchLib(tool=SKIDL).add_parts(*[
        Part(name='AUIPS7111S',dest=TEMPLATE,tool=SKIDL,keywords='Current Sense,High Side Switch',description='Current Sense With High Side Switch 24V/30A, D2PAK-5L',ref_prefix='U',num_units=1,fplist=['TO-263*'],do_erc=True,pins=[
            Pin(num='1',name='IN',do_erc=True),
            Pin(num='2',name='IFB',func=Pin.OUTPUT,do_erc=True),
            Pin(num='3',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='OUT',func=Pin.PWROUT,do_erc=True),
            Pin(num='5',name='OUT',func=Pin.PWROUT,do_erc=True)]),
        Part(name='AUIPS7121R',dest=TEMPLATE,tool=SKIDL,keywords='Current Sense, High Side Switch',description='Current Sense With High Side Switch, 24V/50A, DPAK-5L',ref_prefix='U',num_units=1,fplist=['TO-252*'],do_erc=True,pins=[
            Pin(num='1',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='2',name='IN',do_erc=True),
            Pin(num='3',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='IFB',func=Pin.OUTPUT,do_erc=True),
            Pin(num='5',name='OUT',func=Pin.PWROUT,do_erc=True)]),
        Part(name='IRS2092',dest=TEMPLATE,tool=SKIDL,keywords='Gate Driver Class D',description='Protected Class D Audio Amplifier Half-Bridge Gate Driver, With PWM Modulator, Output Current 1.0/1.2A, +/-100V, PDIP-16/SOIC-16',ref_prefix='U',num_units=1,fplist=['SOIC*3.9x9.9mm*Pitch1.27mm*', 'DIP*W7.62mm*'],do_erc=True,pins=[
            Pin(num='1',name='VAA',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='IN-',do_erc=True),
            Pin(num='4',name='COMP',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='CSD',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='VSS',func=Pin.PWRIN,do_erc=True),
            Pin(num='7',name='VREF',func=Pin.OUTPUT,do_erc=True),
            Pin(num='8',name='OCSET',func=Pin.PASSIVE,do_erc=True),
            Pin(num='9',name='DT',func=Pin.PASSIVE,do_erc=True),
            Pin(num='10',name='COM',func=Pin.PWRIN,do_erc=True),
            Pin(num='11',name='LO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='12',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='13',name='VS',func=Pin.PASSIVE,do_erc=True),
            Pin(num='14',name='HO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='15',name='VB',func=Pin.PWRIN,do_erc=True),
            Pin(num='16',name='CSH',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='IRS20957S',dest=TEMPLATE,tool=SKIDL,keywords='Gate Driver Class D',description='Protected Class D Audio Amplifier Half-Bridge Gate Driver, Output Current 1.0/1.2A, +/-100V, SOIC-16',ref_prefix='U',num_units=1,fplist=['SOIC*3.9x9.9mm*Pitch1.27mm*'],do_erc=True,pins=[
            Pin(num='1',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='CSD',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='IN',do_erc=True),
            Pin(num='4',name='VSS',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='6',name='VREF',func=Pin.OUTPUT,do_erc=True),
            Pin(num='7',name='OCSET',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='DT',func=Pin.PASSIVE,do_erc=True),
            Pin(num='9',name='COM',func=Pin.PWRIN,do_erc=True),
            Pin(num='10',name='LO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='11',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='12',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='13',name='VS',func=Pin.PASSIVE,do_erc=True),
            Pin(num='14',name='HO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='15',name='VB',func=Pin.PWRIN,do_erc=True),
            Pin(num='16',name='CSH',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='IR2104',dest=TEMPLATE,tool=SKIDL,keywords='Gate Driver',description='High and Low Side Gate Driver, Output Current 130/270mA, PDIP-8 , SOIC-8',ref_prefix='U',num_units=1,fplist=['SOIC*3.9x4.9mm*Pitch1.27mm*', 'DIP*W7.62mm*'],do_erc=True,pins=[
            Pin(num='1',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='IN',do_erc=True),
            Pin(num='3',name='~SD',do_erc=True),
            Pin(num='4',name='COM',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='LO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='6',name='VS',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='HO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='8',name='VB',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='IR2106',dest=TEMPLATE,tool=SKIDL,keywords='Gate Driver',description='High and Low Side Driver, 600V operation, Output Current 120/200mA, PDIP-8 , SOIC-8',ref_prefix='U',num_units=1,fplist=['SOIC*', 'DIP*'],do_erc=True,pins=[
            Pin(num='1',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='HIN',do_erc=True),
            Pin(num='3',name='LIN',do_erc=True),
            Pin(num='4',name='COM',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='LO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='6',name='VS',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='HO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='8',name='VB',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='IR2110',dest=TEMPLATE,tool=SKIDL,keywords='Gate Driver',description='High and Low Side Gate Driver, Output Current 2.0/2.0A, PDIP-14 , SOIC-14',ref_prefix='U',num_units=1,fplist=['SOIC*7.5x10.3mm*Pitch1.27mm*', 'DIP*W7.62mm*'],do_erc=True,aliases=['IR2113'],pins=[
            Pin(num='1',name='LO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='2',name='COM',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='5',name='VS',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='VB',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='HO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='8',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='9',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='10',name='HIN',do_erc=True),
            Pin(num='11',name='SD',do_erc=True),
            Pin(num='12',name='LIN',do_erc=True),
            Pin(num='13',name='VSS',func=Pin.PWRIN,do_erc=True),
            Pin(num='14',name='NC',func=Pin.NOCONNECT,do_erc=True)]),
        Part(name='IRS2181',dest=TEMPLATE,tool=SKIDL,keywords='Gate Driver',description='High and Low Side Gate Driver, Output Current 1.4/1.8A, PDIP-8 , SOIC-8',ref_prefix='U',num_units=1,fplist=['SOIC*3.9x4.9mm*Pitch1.27mm*', 'DIP*W7.62mm*'],do_erc=True,pins=[
            Pin(num='1',name='HIN',do_erc=True),
            Pin(num='2',name='LIN',do_erc=True),
            Pin(num='3',name='COM',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='LO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='5',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='6',name='VS',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='HO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='8',name='VB',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='IRS2186',dest=TEMPLATE,tool=SKIDL,keywords='gate driver',description='High and Low Side Gate Driver, 600V operation, 4A output current',ref_prefix='U',num_units=1,fplist=['SOIC*3.9x4.9mm*Pitch1.27mm*', 'DIP*W7.62mm*'],do_erc=True,pins=[
            Pin(num='1',name='HIN',do_erc=True),
            Pin(num='2',name='LIN',do_erc=True),
            Pin(num='3',name='COM',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='LO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='5',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='6',name='VS',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='HO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='8',name='VB',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='IRS21867S',dest=TEMPLATE,tool=SKIDL,keywords='Gate Driver',description='High and Low Side Gate Driver, Output Current 4.0/4.0A, 600V, SOIC-8',ref_prefix='U',num_units=1,fplist=['SOIC*3.9x4.9mm*Pitch1.27mm*'],do_erc=True,pins=[
            Pin(num='1',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='HIN',do_erc=True),
            Pin(num='3',name='LIN',do_erc=True),
            Pin(num='4',name='COM',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='LO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='6',name='VS',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='HO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='8',name='VB',func=Pin.PWRIN,do_erc=True)])])