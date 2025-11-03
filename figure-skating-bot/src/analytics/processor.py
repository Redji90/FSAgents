# processor.py

def analyze_results(results):
    """
    Analyze figure skating results and generate basic analytics.
    
    Args:
        results (list): A list of dictionaries containing figure skating results.
        
    Returns:
        dict: A dictionary containing analysis metrics.
    """
    # Example analysis: Calculate average score
    total_score = sum(result['score'] for result in results)
    average_score = total_score / len(results) if results else 0
    
    return {
        'total_results': len(results),
        'average_score': average_score,
    }

def generate_report(analysis):
    """
    Generate a report based on the analysis of figure skating results.
    
    Args:
        analysis (dict): A dictionary containing analysis metrics.
        
    Returns:
        str: A formatted report string.
    """
    report = f"Total Results: {analysis['total_results']}\n"
    report += f"Average Score: {analysis['average_score']:.2f}\n"
    
    return report