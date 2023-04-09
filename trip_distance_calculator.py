#!/usr/bin/env python
import rospy
import yaml

if __name__ == '__main__':
    rospy.init_node('trip_distance_calculator')

    # Load the odometer values from the YAML file
    with open('odometer.yaml', 'r') as f:
        odometer_values = yaml.safe_load(f)
        start_odometer = odometer_values['start_odometer']
        end_odometer = odometer_values['end_odometer']

    # Calculate the trip distance
    trip_distance = end_odometer - start_odometer

    # Publish the trip distance value to the parameter server
    rospy.set_param('trip_distance', trip_distance)

    rospy.loginfo('Trip distance: {} meters'.format(trip_distance))

# we calculate the trip distance, 
# store the result in the ROS parameter server, 
# and log the calculated trip distance to the console.