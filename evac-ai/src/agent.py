# src/agent.py

from src.rules import EVALUATION_RULES

class EvacuationAgent:
    def __init__(self, building_name, text):
        self.building = building_name
        self.text = text.lower()
        self.findings = {}
        self.vulnerabilities = []
        self.recommendations = []

    def evaluate(self):
        for rule, data in EVALUATION_RULES.items():
            count = sum(self.text.count(keyword) for keyword in data["keywords"])

            passed = count >= data["min_count"]
            self.findings[rule] = {
                "count": count,
                "passed": passed
        }

            if not passed:
                self.vulnerabilities.append(
                    f"{data['description']} (found {count}, expected {data['min_count']})"
            )
                self.recommendations.append(
                    f"Enhance evacuation plan to better address: {data['description']}."
            )

        return self.generate_report()


    def generate_report(self):
        total_rules = len(self.findings)
        failed_rules = len(self.vulnerabilities)

        risk_ratio = failed_rules / total_rules

        if risk_ratio == 0:
            risk_level = "Low"
        elif risk_ratio <= 0.5:
            risk_level = "Medium"
        else:
            risk_level = "High"
        return {
            "building": self.building,
            "risk_level": risk_level,
            "vulnerabilities": self.vulnerabilities,
            "recommendations": self.recommendations,
            "details": self.findings
        }
