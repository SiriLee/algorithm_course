def activity_selection(activities):
    """
    Selects the maximum number of activities that can be performed by a single person,
    assuming that a person can only work on a single activity at a time.

    :param activities: A list of tuples, where each tuple contains the start and end time of an activity.
                       Example: [(start1, end1), (start2, end2), ...]
    :return: A list of selected activities that can be performed.
    """
    # Sort activities based on their finish time
    sorted_activities = sorted(activities, key=lambda x: x[1])

    selected_activities = []
    last_end_time = 0

    for activity in sorted_activities:
        start_time, end_time = activity
        if start_time >= last_end_time:
            selected_activities.append(activity)
            last_end_time = end_time

    return selected_activities
