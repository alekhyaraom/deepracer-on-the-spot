def reward_function(params):
    '''
    Example of a reward function for AWS DeepRacer on the Ross Raceway track.
    '''

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    steering_angle = abs(params['steering_angle'])  # Only need the absolute steering angle

    # Calculate 3 markers that are at varying distances from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Reward based on distance from the center line
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    # Penalize if the car is off track
    if not all_wheels_on_track:
        reward = 1e-3

    # Reward for the car's speed
    # Increase the reward non-linearly for higher speeds
    reward += (speed ** 2) * 0.1

    # Penalize for steering too much to prevent zigzag behavior
    ABS_STEERING_THRESHOLD = 15.0
    if steering_angle > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    return float(reward)
