import time
import pytest
from SpannerTestboard import SpannerTestboard

from ut61e_py.UT61E import UT61E
import datetime


testboard = SpannerTestboard("xenonEthDev3")


CHARGER_RELAY_PIN = "D2"
LOAD_RELAY_PIN = "D6"

GREEN_LED_PIN = "A3"
RED_LED_PIN = "A4"


TEMP_PIN = "A0"

DIVIDER_PIN = "A2"

def test_measure_power_consumption():
    print("")
    testboard.digitalWrite(CHARGER_RELAY_PIN, 'LOW')
    testboard.digitalWrite(LOAD_RELAY_PIN, 'LOW')
    testboard.digitalWrite(GREEN_LED_PIN, 'LOW')
    testboard.digitalWrite(RED_LED_PIN, 'LOW')
    time.sleep(5)

    INA219 = SpannerTestboard.INA219
    testboard.ina219_setGainOne()

    print("Measuring Shunt Voltage & Current")
    shunt_voltage_mv = testboard.ina219_getValue(INA219.SHUNT_VOLTAGE_MV)
    current_multiplier = 5
    current = testboard.ina219_getValue(INA219.CURRENT_MA) * current_multiplier

    print("Current consumption (mA):")
    print(current)

    print("Shunt Voltage (mV):")
    print(shunt_voltage_mv)

    print("Shunt Current consumption (mA):")
    shunt_resistor = 0.02
    current = (shunt_voltage_mv) /  shunt_resistor
    print(current)

    testboard.digitalWrite(CHARGER_RELAY_PIN, 'HIGH')
    testboard.digitalWrite(LOAD_RELAY_PIN, 'HIGH')
    testboard.digitalWrite(GREEN_LED_PIN, 'HIGH')
    testboard.digitalWrite(RED_LED_PIN, 'HIGH')

    temperature = get_temperature(TEMP_PIN)
    print("Temperature: " + str(temperature))

    meas=testboard.analogRead(DIVIDER_PIN)
    divider_voltage = float(meas)/4096 * 3.3
    print("Divider voltage: " + str(divider_voltage))

    dmm = UT61E(testboard)
    meas = dmm.get_meas()
    # {'mode': 'V/mV', 'range': '22.000', 'val': 12.422, 'units': 'V', 'norm_val': 12.422, 'norm_units': 'V',
    #  'percent': False, 'minus': False, 'low_bat': False, 'ovl': False, 'delta': False, 'ul': False, 'max': False,
    #  'min': False, 'dc': True, 'ac': False, 'auto': True, 'hz': False, 'hold': False, 'data_valid': True}
    print("Timestamp: ", datetime.datetime.now())
    print(meas)

    assert meas["data_valid"]
    assert meas["mode"] == "V/mV"
    assert meas["dc"]
    assert meas["hold"] == False
    assert meas["norm_units"] == "V"
    assert meas["norm_val"] > 12


    time.sleep(10)

    testboard.digitalWrite(CHARGER_RELAY_PIN, 'LOW')
    testboard.digitalWrite(LOAD_RELAY_PIN, 'LOW')
    testboard.digitalWrite(GREEN_LED_PIN, 'LOW')
    testboard.digitalWrite(RED_LED_PIN, 'LOW')


#get the current temperature.
def get_temperature(tmp_pin):
  value = testboard.analogRead(tmp_pin)
  print(value)
  voltage = (3.3 * value) / 4096
  print(voltage)
  return (voltage - 0.5) * 100


