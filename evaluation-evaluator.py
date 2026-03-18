def evaluate_response(question, answer, context):
    """
    Simple evaluation placeholder (extend with RAGAS later)
    """
    score = 0

    if answer and len(answer) > 20:
        score += 1

    if any(c.lower() in answer.lower() for c in context):
        score += 1

    return {
        "question": question,
        "score": score,
        "max_score": 2
    }