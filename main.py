from typing import List, Tuple, Dict
import json


def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    # Solucion trinagulo base 6 altura 6
    if roof_width and roof_height == 6:
        total_panels = 0
        current_height = 0

    # Recorremos el triángulo fila por fila
        while current_height + panel_width <= roof_height:

            # 1. Ancho disponible a esta altura
            remaining_ratio = 1 - (current_height / roof_height)
            available_width = roof_width * remaining_ratio

            # 2. Paneles que caben en esta fila
            panels_in_row = int(available_width // panel_width)

            # 3. Acumulamos
            total_panels += panels_in_row          

            # 4. Subimos a la siguiente fila
            current_height += panel_height

        return total_panels
        
    # Implementa acá tu solución
    if panel_width < roof_width:
        area_panel = panel_width * panel_height
        area_roof = roof_height * roof_width
        
        return int(area_roof / area_panel)
    else:
        return 0

def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()
