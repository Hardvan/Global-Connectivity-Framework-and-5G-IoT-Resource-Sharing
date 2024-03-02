"""Contains the sorting algorithm for the distribution of the ratio lists of latency and load.
"""


def selection_sort(ratio_list, threshold=0.75):

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
                print("❌ Cannot Distribute Load in this Region")
                print("Continuing anyway...")

            # Updating
            ratio_list[i] = ratio
            ratio_list[least_ratio_index] = least_ratio

    return ratio_list
