# src/analyzer.py

from src.agent import EvacuationAgent

def analyze_building(building_name, file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    agent = EvacuationAgent(building_name, text)
    report = agent.evaluate()

    return report
