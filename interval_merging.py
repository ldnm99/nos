def merge_intervals(intervals):
    """
    Merges overlapping intervals in a list.

    Args:
        intervals (List[List[int]] or List[Tuple[int, int]]): 
            A list of intervals, where each interval is a pair [start, end] or (start, end).

    Returns:
        List[List[int]] or List[Tuple[int, int]]: 
            A list of merged intervals, where overlapping intervals are combined.

    Time Complexity: O(n log n) due to sorting.
    Space Complexity: O(n) in the worst case (if no intervals merge).
    """

    # if the input list is empty, return an empty list
    if not intervals:
        return []

    # if each interval is a valid list or tuple of two elements
    for interval in intervals:
        if not isinstance(interval, (list, tuple)) or len(interval) != 2:
            raise ValueError("Each interval must have two elements.")
        
        start, end = interval
        # if both start and end are integers or floats
        if not all(isinstance(x, (int, float)) for x in interval):
            raise ValueError("All elements in the arrays must be integers or floats.")
        
        # if the start value is greater than the end value
        if start > end:
            raise ValueError("Start value cannot be greater than end value.")
        
    # sort the intervals based on the start value 
    intervals.sort(key = lambda x: x[0])

    # final list with the start value of the first interval aka the lowest boundary
    final = [intervals[0]]

    for start, end in intervals[1:]:
        # last interval in the final list
        last_start, last_end = final[-1]

        # if the current interval overlaps with the last final interval
        if start <= last_end:
            # merge overlapping intervals by updating the last interval end
            # new end value is the max of the current interval end and the last final interval 
            final[-1] = [last_start, max(last_end, end)]
        else:
            # if no overlap add the interval in the final list
            final.append([start, end])

    return final
