from rules import RULES

def evaluate_state(input_data):
    violations = []
    confidence = input_data.get("confidence", 0)

    if confidence < RULES["min_confidence"]:
        violations.append("confidence_below_threshold")

    if not input_data.get("evidence"):
        violations.append("missing_evidence")

    if input_data.get("source") not in RULES["valid_sources"]:
        violations.append("invalid_source")

    admissible = len(violations) == 0

    corrected_state = {}
    if not admissible:
        corrected_state = {
            "confidence": max(confidence, RULES["min_confidence"]),
            "source": "verified_db"
        }

    return {
        "admissible": admissible,
        "confidence": confidence,
        "violations": violations,
        "corrected_state": corrected_state
    }
