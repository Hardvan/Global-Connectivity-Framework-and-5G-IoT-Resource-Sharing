"""Contains the sorting algorithm for the distribution of the ratio lists of latency and load.
"""


def selection_sort(ratio_list, threshold=0.75):
    """Distributes the ratios in the list to ensure that no ratio exceeds the threshold value.

    Methodology
    -----------
    1. If the current ratio 'r' exceeds the threshold value, then the difference between r and the threshold is calculated.
    2. The difference is then added to the least ratio in the list.
    3. r is then reduced by the difference.
    4. The least ratio is increased by the difference.
    5. The ratio list is updated with the new values.
    6. The process is repeated for all the ratios in the list.

    Time Complexity
    ---------------
    O(n²): Outer loop runs n times, and the inner loop runs n times (finding the least ratio in the list).

    Space Complexity
    ----------------
    O(1): No extra space is used.

    Args
    ----
    - ratio_list: List of ratios to be distributed.
    - threshold: The max value of the ratio that is allowed.

    Returns
    -------
    - ratio_list: The list of ratios after distribution.
    """

    # Deep copy of the list
    ratio_list = ratio_list[:]

    for i in range(len(ratio_list)):

        ratio = ratio_list[i]
        if ratio >= threshold:  # Ratio exceeds threshold value, then exchange

            difference = ratio - threshold

            # Find the least ratio and its index
            least_ratio = min(ratio_list)
            least_ratio_index = ratio_list.index(least_ratio)

            if least_ratio + difference <= 0.75:  # Distributing Load only if Lower Bar after addition is < threshold
                ratio -= difference
                least_ratio += difference
            else:
                print("❌ Cannot Distribute ratios in this Region")
                print("Continuing anyway...")

            # Updating
            ratio_list[i] = ratio
            ratio_list[least_ratio_index] = least_ratio

    return ratio_list


def linear_sort(ratio_list, threshold=0.75):
    """Distributes the ratios in the list to ensure that no ratio exceeds the threshold value.

    Methodology
    -----------
    1. Create a 'buffer' variable that stores the excess ratio (exceeding threshold).
    2. Iterate over the list of ratios
        2.1 if ratio >= threshold, then add the excess (ratio - threshold) to the buffer, set the ratio to threshold.
    3. Iterate over the list of ratios
        3.1 if ratio < threshold, then add that much from the buffer to the ratio such that new_ratio = 70% of threshold (soft limit).
    4. If some amount is still left in buffer, then again iterate over the list of ratios and add the remaining buffer to the ratios, even if they reach 100% of threshold (hard limit).
    4. Return the updated ratio list.

    Args
    ----
    - ratio_list: List of ratios to be distributed.
    - threshold: The max value of the ratio that is allowed.

    Returns
    -------
    """

    n = len(ratio_list)

    buffer = 0
    for i in range(n):
        if ratio_list[i] >= threshold:
            buffer += ratio_list[i] - threshold
            ratio_list[i] = threshold

    for i in range(n):
        if ratio_list[i] < threshold:
            required = 0.7 * threshold - ratio_list[i]  # Soft Limit
            if buffer > required:
                ratio_list[i] += required
                buffer -= required
            else:
                ratio_list[i] += buffer
                buffer = 0

    if buffer > 0:
        for i in range(n):
            required = threshold - ratio_list[i]
            if buffer > required:
                ratio_list[i] += required
                buffer -= required
            else:
                ratio_list[i] += buffer
                buffer = 0

    if buffer > 0:
        print("❌ Buffer is still not empty. Some ratios is still left to be distributed.")
        print("Continuing anyway...")

    return ratio_list


if __name__ == '__main__':
    print("Testing the distribute module...")

    ratio_list = [0.8, 0.9, 0.7, 0.6, 0.8, 0.4, 0.7,
                  0.2, 0.1, 0.3, 0.7, 0.6, 0.8, 0.9, 0.7, 0.6]
    print(
        f"Original Ratio List: {ratio_list}, sum of ratios: {sum(ratio_list):.2f}")
    selection_sort_ratio_list = selection_sort(ratio_list)
    print(
        f"After Selection Sort: {selection_sort_ratio_list}, sum of ratios: {sum(selection_sort_ratio_list):.2f}")
    linear_sort_ratio_list = linear_sort(ratio_list)
    print(
        f"After Linear Sort: {linear_sort_ratio_list}, sum of ratios: {sum(linear_sort_ratio_list):.2f}")
