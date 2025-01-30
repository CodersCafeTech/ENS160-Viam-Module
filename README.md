# [ens160 modular service](https://app.viam.com/module/coderscafe/ens160)
This module implements the [rdk sensor API](https://github.com/rdk/sensor-api) in a coderscafe:sensor:ens160 model.
With this model, you can read VOCs (volatile organic compounds), eCO2 (equivalent carbon dioxide), and an Air Quality Index (AQI) from [DFRobot Fermion: ENS160 Air Quality Sensor](https://www.dfrobot.com/product-2523.html)

## Requirements
Please make sure that [I2C communication is enabled](https://docs.viam.com/operate/reference/prepare/rpi-setup/#enable-communication-protocols) on the device to which the sensor is connected.

## Build and Run

To use this module, follow these instructions to [add a module from the Viam Registry](https://docs.viam.com/registry/configure/#add-a-modular-resource-from-the-viam-registry) and select the [`coderscafe:sensor:ens160` module](https://app.viam.com/module/coderscafe/ens160).

## Configure your sensor

> [!NOTE]  
> Before configuring your sensor, you must [create a machine](https://docs.viam.com/manage/fleet/machines/#add-a-new-machine).

* Navigate to the **Config** tab of your robot’s page in [the Viam app](https://app.viam.com/).
* Click on the **Components** subtab and click on the `sensor` subtab.
* Select the `coderscafe:sensor:ens160` model. 
* Enter a name for your sensor and click **Create**.
* Save and wait for the component to finish setup.

> [!NOTE]  
> For more information, see [Configure a Robot](https://docs.viam.com/manage/configuration/).

### Attributes

The following attributes are available for `rdk:sensor:coderscafe:sensor:ens160` sensor:

| Name | Type | Inclusion | Description |
| ---- | ---- | --------- | ----------- |
| `temperature_compensation` | integer | Optional |  Set Temperature Compensation |
| `humidity_compensation` | integer | Optional |  Set Humidity Compensation |

### Example Configuration

```json
{
  "temperature_compensation":30,
  "humidity_compensation": 60
}
```

