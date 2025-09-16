import tkinter as tk
from tkinter import ttk
import mock_state_manager as sm

class PlantCareGUI:
    def __init__(self, root):
        self.root = root
        root.title("PlantCarePi")

        # Title
        ttk.Label(root, text="PlantCarePi GUI", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=3, pady=10)

        # Sensor Readout
        self.temp_label = ttk.Label(root, text="Temp: -- °C")
        self.rh_label = ttk.Label(root, text="Humidity: -- %")
        self.soil_label = ttk.Label(root, text="Soil Moisture: --")
        self.lux_label = ttk.Label(root, text="Lux: --")

        self.temp_label.grid(row=1, column=0, padx=10)
        self.rh_label.grid(row=1, column=1, padx=10)
        self.soil_label.grid(row=1, column=2, padx=10)
        self.lux_label.grid(row=1, column=3, padx=10)

        # Actuator Controls
        self.pump_button = ttk.Button(root, text="Toggle Pump", command=self.toggle_pump)
        self.uv_button = ttk.Button(root, text="Toggle UV", command=self.toggle_uv)
        self.heater_button = ttk.Button(root, text="Toggle Heater", command=self.toggle_heater)
        self.cooler_button = ttk.Button(root, text="Toggle Cooler", command=self.toggle_cooler)

        self.pump_button.grid(row=2, column=0, pady=10)
        self.uv_button.grid(row=2, column=1, pady=10)
        self.heater_button.grid(row=2, column=2, pady=10)
        self.cooler_button.grid(row=2, column=3, pady=10)

        # Sliders
        self.fan_slider = ttk.Scale(root, from_=0, to=100, command=self.set_fan)
        self.fan_slider.set(50)
        ttk.Label(root, text="Fan Speed (%)").grid(row=3, column=0)
        self.fan_slider.grid(row=3, column=1)

        self.servo_slider = ttk.Scale(root, from_=0, to=180, command=self.set_servo)
        self.servo_slider.set(90)
        ttk.Label(root, text="Servo Angle").grid(row=3, column=2)
        self.servo_slider.grid(row=3, column=3)

        # Status Labels
        self.status_label = ttk.Label(root, text="System OK")
        self.status_label.grid(row=4, column=0, columnspan=2)

        self.logging_label = ttk.Label(root, text="Logging: OFF")
        self.logging_label.grid(row=4, column=2, columnspan=2)

        # Periodic update
        self.update_labels()
        self.root.after(1000, self.update_loop)

    def update_labels(self):
        state = sm.get_state()
        self.temp_label.config(text=f"Temp: {state['temp_c']} °C")
        self.rh_label.config(text=f"Humidity: {state['rh']} %")
        self.soil_label.config(text=f"Soil Moisture: {state['soil']}")
        self.lux_label.config(text=f"Lux: {state['lux']}")

    def update_loop(self):
        sm.update_fake_sensors()
        self.update_labels()
        self.root.after(1000, self.update_loop)

    # Control Functions
    def toggle_pump(self):
        current = sm.get_state()["pump"]
        sm.set_actuator("pump", not current)

    def toggle_uv(self):
        current = sm.get_state()["uv"]
        sm.set_actuator("uv", not current)

    def toggle_heater(self):
        current = sm.get_state()["heater"]
        sm.set_actuator("heater", not current)

    def toggle_cooler(self):
        current = sm.get_state()["cooler"]
        sm.set_actuator("cooler", not current)

    def set_fan(self, val):
        sm.set_actuator("fan", int(float(val)))

    def set_servo(self, val):
        sm.set_actuator("servo", int(float(val)))

# Main entry
if __name__ == "__main__":
    root = tk.Tk()
    app = PlantCareGUI(root)
    root.mainloop()
