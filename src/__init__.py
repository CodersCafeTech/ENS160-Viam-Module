"""
This file registers the model with the Python SDK.
"""

from viam.components.sensor import Sensor
from viam.resource.registry import Registry, ResourceCreatorRegistration

from .ens160 import ens160

Registry.register_resource_creator(Sensor.SUBTYPE, ens160.MODEL, ResourceCreatorRegistration(ens160.new, ens160.validate))
