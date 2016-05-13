# Summative Task

## Overall goal

My summative task will be a combination software and hardware product.

I will program a sensor attached to an Arduino board. The sensor will be able to detect how hard a person is blowing air toward it (perhaps a pressure sensor? a mic?).

When a person blows on the sensor, this information is transmitted to a Processing sketch.

In the sketch, a visual representation of a "ripe" dandelion will be shown.  The dandelion seeds will disperse on screen in the sketch, simulating the physics of the motion of real dandelion seeds, when someone blows them off the stem in real life.

## Sub-goals

* extend Motion class (that we developed earlier together) to allow for force accumulation (wind, gravity, other forces)
* make the mouse movement translate to a wind force
* make it so that moving the mouse causes the "seeds" of the dandelion to disperse
* modify the visual representation of the Motion class to more closely resembly dandelion seeds
* identify an Arduino sensor that might work to detect air pressure / volume
* program sensor to send values to Processing sketch
* translate sensor output to wind force in sketch
