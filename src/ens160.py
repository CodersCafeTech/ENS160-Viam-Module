from typing import ClassVar, Mapping, Sequence, Any, Dict, Optional, Tuple, Final, List, cast, Union
from typing_extensions import Self

from viam.utils import SensorReading
from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName, Vector3
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily

from viam.components.sensor import Sensor
from viam.logging import getLogger

import time
import asyncio

import board
import adafruit_ens160
import asyncio

LOGGER = getLogger(__name__)

class ens160(Sensor, Reconfigurable):
    """
    A Viam Sensor implementation for the ENS160 air quality sensor.
    """

    MODEL: ClassVar[Model] = Model(ModelFamily("coderscafe", "sensor"), "ens160")

    def __init__(self, name: str):
        super().__init__(name)
        self.i2c = board.I2C()  # Uses board.SCL and board.SDA
        try:
            self.i2c = board.I2C()
            self.ens = adafruit_ens160.ENS160(self.i2c)
        except Exception as e:
            LOGGER.error(f"Failed to initialize ENS160 sensor: {e}")
            raise
        self.ens.temperature_compensation = 25  # Set default temperature compensation
        self.ens.humidity_compensation = 50    # Set default humidity compensation

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        sensor_instance = cls(config.name)
        sensor_instance.reconfigure(config, dependencies)
        return sensor_instance

    @classmethod
    def validate(cls, config: ComponentConfig):
        # Validate configuration if necessary. Add checks as needed.
        return

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        # Reconfigure sensor parameters if provided in config attributes.
        if "temperature_compensation" in config.attributes.fields:
            self.ens.temperature_compensation = config.attributes.fields["temperature_compensation"].number_value
        if "humidity_compensation" in config.attributes.fields:
            self.ens.humidity_compensation = config.attributes.fields["humidity_compensation"].number_value
        return
    
    async def get_readings(
        self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, SensorReading]:
        """
        Obtain air quality data from the ENS160 sensor.
        
        Returns:
            Mapping[str, SensorReading]: A dictionary containing AQI, TVOC, and eCO2 readings.
        """
        try:
            readings = {
                "AQI": self.ens.AQI,
                "TVOC": self.ens.TVOC,
                "eCO2": self.ens.eCO2,
            }
            return readings
        except Exception as e:
            LOGGER.error(f"Failed to read from ENS160 sensor: {e}")
            raise
