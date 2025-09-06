# 🔧 Function Tree Simulation for a Smart Component

class FunctionNode:
    def _init_(self, name, knowledge, data, power):
        self.name = name
        self.knowledge = knowledge  # e.g., electronics, thermodynamics
        self.data = data            # e.g., sensor input/output
        self.power = power          # in watts
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def total_power(self):
        return self.power + sum(child.total_power() for child in self.children)

    def display(self, level=0):
        indent = "  " * level
        print(f"{indent}- {self.name} | Knowledge: {self.knowledge} | Data: {self.data} | Power: {self.power}W")
        for child in self.children:
            child.display(level + 1)

# 🌳 Build Function Tree
root = FunctionNode("Smart Bottle System", "System Design", "User Input", 0.5)
sensor = FunctionNode("Temperature Sensor", "Thermodynamics", "Temp Data", 0.1)
display = FunctionNode("LED Display", "Electronics", "Visual Output", 0.2)
battery = FunctionNode("Battery Unit", "Power Systems", "Energy Supply", 0.3)

root.add_child(sensor)
root.add_child(display)
root.add_child(battery)

# 🧮 Output Tree and Power Summary
root.display()
print(f"\n🔋 Total Power Required: {root.total_power()}W")

# 🧪 Component Design Simulation (Sensor)
def design_sensor(length_mm, diameter_mm, material_density):
    volume_cm3 = 3.14 * (diameter_mm / 20)**2 * (length_mm / 10)  # cm³
    mass_g = volume_cm3 * material_density  # g
    print(f"\n📐 Sensor Design: Length={length_mm}mm, Diameter={diameter_mm}mm")
    print(f"Estimated Mass: {mass_g:.2f}g")

design_sensor(length_mm=50, diameter_mm=10, material_density=1.2)  # ABS plastic

# 🏭 Manufacturing & Material Justification
manufacturing_process = "Injection Molding"
material_choice = "ABS Plastic"
joining_method = "Snap-fit"

print(f"\n🏭 Manufacturing: {manufacturing_process}")
print(f"🧱 Material: {material_choice}")
print(f"🔩 Joining Method: {joining_method}")