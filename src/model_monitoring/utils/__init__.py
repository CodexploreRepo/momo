import numpy as np


def normalize_min_max(input: np.ndarray) -> np.ndarray:
    # Scales input vector to [0,1] using min-max scaler
    # norm_input = (input - min)/(max-min)
    min_value, max_value = np.min(input),  np.max(input)
    return np.divide((input-min_value).astype(float), (max_value-min_value).astype(float), out=np.zeros_like(input).astype(float), where=input != 0)


def scale_to_range(input: np.ndarray, lower, upper) -> np.ndarray:
    # Scales input to [lower, upper]
    input = normalize_min_max(input)*(upper - lower) + lower
    return input


def normalize_data_length(ref_arr: np.ndarray, curr_arr: np.ndarray, buckets=10, bucket_type='bins') -> dict:
    """
    Data length normalizer will normalize a set of data points if (ref_arr, curr_arr)
    are not the same length by bucketizing curr_arr into the breakpoints of ref_arr
    i.e: normalize 2 numerical arrays (ref_arr, curr_arr) by binning them into same buckets

    params:
        ref_data (List) : The numpy array of values associated with the training data
        curr_data (List) : The numpy array of values associated with the curr data
        bins (Int) : The number of bins you want to use for the distributions

    returns:
        The ground truth and observation data in the same length.
    """
    # *100: use to compute percentile, 0%, 5, 10, 15
    breakpoints = np.arange(0, buckets + 1) / (buckets) * 100
    # breakpoints based on the ref sample (i.e: sample_1)
    if bucket_type == 'bins':
        breakpoints = scale_to_range(
            breakpoints, np.min(ref_arr), np.max(ref_arr))
    elif bucket_type == 'quantiles':
        breakpoints = np.array([np.percentile(ref_arr, b)
                               for b in breakpoints])

    ref_hist, bins = np.histogram(ref_arr, breakpoints)
    curr_hist, _ = np.histogram(curr_arr, breakpoints)
    bins = 0.5*(bins[:-1] + bins[1:])

    return {'ref_hist': ref_hist,
            'curr_hist': curr_hist,
            'bins': bins
            }
