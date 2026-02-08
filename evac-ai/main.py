# main.py

from src.analyzer import analyze_building

buildings = {
    "Elizabeth Hall": "data/ElizabethHall.txt",
    "Brown Hall": "data/BrownHall.txt",
    "Flagler Hall": "data/FlaglerHall.txt",
    "Chadouin Hall": "data/ChadouinHall.txt",
    "Emily Hall": "data/EmilyHall.txt",
    "Lynn Hall": "data/LynnHall.txt",
}

for building, path in buildings.items():
    report = analyze_building(building, path)

    print("\n==============================")
    print(f"Building: {report['building']}")
    print(f"Risk Level: {report['risk_level']}")
    print("Vulnerabilities:")
    for v in report["vulnerabilities"]:
        print(f" - {v}")
    print("Recommendations:")
    for r in report["recommendations"]:
        print(f" - {r}")
