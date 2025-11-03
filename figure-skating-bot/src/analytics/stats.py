# stats.py

def calculate_average_score(scores):
    """Calculate the average score from a list of scores."""
    if not scores:
        return 0
    return sum(scores) / len(scores)

def calculate_highest_score(scores):
    """Return the highest score from a list of scores."""
    if not scores:
        return 0
    return max(scores)

def calculate_lowest_score(scores):
    """Return the lowest score from a list of scores."""
    if not scores:
        return 0
    return min(scores)

def calculate_score_distribution(scores):
    """Calculate the distribution of scores."""
    distribution = {}
    for score in scores:
        if score in distribution:
            distribution[score] += 1
        else:
            distribution[score] = 1
    return distribution