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

    # If the input list is empty, return an empty list
    if not intervals:
        return []

    # Sort the intervals based on the start time (first value in each pair)
    # Sorting ensures that overlapping intervals are adjacent in the list.
    intervals.sort(key = lambda x: x[0])

    # Initialize the final list with the start value of the first interval aka the lowest boundary
    final = [intervals[0]]

    # Iterate over the remaining intervals
    for start, end in intervals[1:]:
        # Get the last interval in the final list
        last_start, last_end = final[-1]

        # Check if the current interval overlaps with the last final interval
        if start <= last_end:
            # Merge overlapping intervals by updating the last interval's end time
            # The new end time is the max of the current interval's end and the last final interval's end
            final[-1] = [last_start, max(last_end, end)]
        else:
            # If no overlap, add the current interval as a new entry in the final list
            final.append([start, end])

    # Return the list of final intervals
    return final
