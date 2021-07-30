#import all required libraries and methods

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color, Rectangle
import json, glob
from datetime import datetime
from pathlib import Path
import random
import math
from kivy.core.window import Window
#....................................................
#...................................................

#Loads kivy file for the design of
Builder.load_file("design.kv")

#............................................
#...........................................

#Screen 1: Main page with buttons for going into other pages
# within the main screen class, each button needs to be defined to connect to its own class through the widget tool
class MainScreen(Screen):
    def mechanics(self):
        self.manager.current = "mechanical_screen"
    def force(self):
        self.manager.current = "force_screen"
    def weight(self):
        self.manager.current = "weight_screen"
    def work(self):
        self.manager.current = "work_screen"
    def power(self):
        self.manager.current = "power_screen"
    def efficiency(self):
        self.manager.current = "efficiency_screen"
    def energy(self):
        self.manager.current = "energy_screen"
    def fluid(self):
        self.manager.current = "fluid_screen"
    def electricity(self):
        self.manager.current = "electricity_screen"
#............................................
#functions for the mechanical screen
class MechanicalScreen(Screen):
    def backwards(self):
        self.manager.transition.direction="right"
        self.manager.current = "main_screen"
    def speed(self):
        self.manager.current = "speed_screen"
    def acceleration(self):
        self.manager.current = "acceleration_screen"
    def suvat_velocity(self):
        self.manager.current = "suvat_velocity_screen"
    def suvat_velocity_2(self):
        self.manager.current = "suvat_velocity_2_screen"
    def suvat_displacement(self):
        self.manager.current = "suvat_displacement_screen"
    def suvat_displacement_2(self):
        self.manager.current = "suvat_displacement_2_screen"

#...............................................

#................................................
#functions for the speed screen
class SpeedScreen(Screen):
    def backwards1(self):
        self.manager.transition.direction="right"
        self.manager.current = "mechanical_screen"
    def get_speed_answer(self,distance,time):
        if self.ids.distance.text == "" or self.ids.time.text == "":
            self.ids.speed_answer.text = "Please fill in variables correctly"   
        else:
            distance = float(distance) 
            time = float(time)
            calc_answer = str(distance / time)
            self.ids.speed_answer.text = str(calc_answer)            
        
#.................................................
#functions for the acceleration screen
class AccelerationScreen(Screen):
    def backwards1(self):
        self.manager.transition.direction="right"
        self.manager.current = "mechanical_screen"
    def get_acceleration_answer(self,velocity,time):
        if self.ids.velocity.text == "" or self.ids.time.text == "":
            self.ids.acceleration_answer.text = "Please fill in variables correctly"          
        else:
            velocity = float(velocity)
            time = float(time)
            calc_answer = (velocity / time)
            self.ids.acceleration_answer.text = str(calc_answer)
#.................................................
#functions for the velocity screen
class SuvatVelocityScreen(Screen):
    def backwards1(self):
        self.manager.transition.direction="right"
        self.manager.current = "mechanical_screen"
    def get_suvat_velocity_answer(self,initial_velocity,acceleration,time):
        if self.ids.initial_velocity.text == "" or self.ids.time.text == "" or self.ids.acceleration.text == "":
            self.ids.suvat_velocity_answer.text = "Please fill in variables correctly"
        else:
            initial_velocity = float(initial_velocity)
            acceleration = float(acceleration)       
            time = float(time)
            calc_answer = (initial_velocity + (acceleration * time))
            self.ids.suvat_velocity_answer.text = str(calc_answer) 
#.................................................
#functions for the velocity 2 screen
class SuvatVelocity2Screen(Screen):
    def backwards1(self):
        self.manager.transition.direction="right"
        self.manager.current = "mechanical_screen"
    def get_suvat_velocity_2_answer(self,initial_velocity,acceleration,displacement):
        if self.ids.initial_velocity.text == "" or self.ids.acceleration.text == "" or self.ids.displacement.text == "":
            self.ids.suvat_velocity_2_answer.text = "Please fill in variables correctly"        
        else:
            initial_velocity = float(initial_velocity)
            acceleration = float(acceleration)       
            displacement = float(displacement)
            calc_answer = ((initial_velocity*initial_velocity) + (2 * acceleration * displacement))
            self.ids.suvat_velocity_2_answer.text = str(math.sqrt(calc_answer)) 
#.................................................
#functions for the displacement screen
class SuvatDisplacementScreen(Screen):
    def backwards1(self):
        self.manager.transition.direction="right"
        self.manager.current = "mechanical_screen"
    def get_suvat_displacement_answer(self,initial_velocity,acceleration,time):
        if self.ids.initial_velocity.text == "" or self.ids.time.text == "" or self.ids.acceleration.text == "":
            self.ids.suvat_displacement_answer.text = "Please fill in variables correctly"
        else:
            initial_velocity = float(initial_velocity)
            acceleration = float(acceleration)       
            time = float(time)
            calc_answer = ((initial_velocity*time)+ (0.5*acceleration*(time*time)))
            self.ids.suvat_displacement_answer.text = str(math.sqrt(calc_answer)) 
#...................................................
#functions for the displacement 2 screen
class SuvatDisplacement2Screen(Screen):
    def backwards1(self):
        self.manager.transition.direction="right"
        self.manager.current = "mechanical_screen"    
    def get_suvat_displacement_2_answer(self,initial_velocity,final_velocity,time):
        if self.ids.initial_velocity.text == "" or self.ids.final_velocity.text == "" or self.ids.time.text == "":
            self.ids.suvat_displacement_2_answer.text = "Please fill in variables correctly"
        else:
            initial_velocity = float(initial_velocity)
            final_velocity = float(final_velocity)       
            time = float(time)
            calc_answer = (0.5*(initial_velocity+final_velocity)*time)
            self.ids.suvat_displacement_2_answer.text = str(calc_answer) 
#...................................................

#functions for the force screen
class ForceScreen(Screen):
    def backwards(self):
        self.manager.transition.direction="right"
        self.manager.current = "main_screen"
    def get_force_answer(self,mass,acceleration):
        if self.ids.mass.text == "" or self.ids.acceleration.text == "":
            self.ids.force_answer.text = "Please fill in variables correctly"
        else:
            mass = float(mass)
            acceleration = float(acceleration)
            calc_answer = (mass * acceleration)
            self.ids.force_answer.text = str(calc_answer) 

#.................................................
#functions for the weight screen
class WeightScreen(Screen):
    def backwards(self):
        self.manager.transition.direction="right"
        self.manager.current = "main_screen"
    def get_weight_answer(self,mass):
        if self.ids.mass.text == "":
            self.ids.weight_answer.text = "Please fill in variable correctly"        
        else:
            mass = float(mass)
            acceleration = 9.81
            calc_answer = (mass * acceleration)
            self.ids.weight_answer.text = str(calc_answer) 
#.................................................
#functions for the work screen
class WorkScreen(Screen):
    def backwards(self):
        self.manager.transition.direction="right"
        self.manager.current = "main_screen"
    def get_work_answer(self,force,displacement):
        if self.ids.force.text == "" or self.ids.displacement.text == "":
            self.ids.work_answer.text = "Please fill in variables correctly"        
        else:
            force = float(force)
            displacement = float(displacement)
            calc_answer = (force * displacement)
            self.ids.work_answer.text = str(calc_answer) 
#.................................................
#functions for the power screen
class PowerScreen(Screen):
    def backwards(self):
        self.manager.transition.direction="right"
        self.manager.current = "main_screen"
    def power1(self):
        self.manager.current = "power1_screen"
    def power2(self):
        self.manager.current = "power2_screen"

#.................................................
#functions for the power1 screen
class Power1Screen(Screen):
    def backwards2(self):
        self.manager.transition.direction="right"
        self.manager.current = "power_screen" 
    def get_power1_answer(self,energy,time):
        if self.ids.energy.text == "" or self.ids.time.text == "":
            self.ids.power1_answer.text = "Please fill in variables correctly"        
        else:
            energy = float(energy)
            time = float(time)
            calc_answer = (energy / time)
            self.ids.power1_answer.text = str(calc_answer) 
#................................................
#functions for the power2 screen
class Power2Screen(Screen):
    def backwards2(self):
        self.manager.transition.direction="right"
        self.manager.current = "power_screen"
    def get_power2_answer(self,torque,rpm):
        if self.ids.torque.text == "" or self.ids.rpm.text == "":
            self.ids.power2_answer.text = "Please fill in variables correctly"
        else:
            torque = float(torque)
            rpm = float(rpm)
            calc_answer = ((torque*rpm)/5252)
            self.ids.power2_answer.text = str(calc_answer) 
#.................................................
#functions for the efficiency screen
class EfficiencyScreen(Screen):
    def backwards(self):
        self.manager.transition.direction="right"
        self.manager.current = "main_screen"
    def get_efficiency_answer(self,ouput,input):
        if self.ids.output.text == "" or self.ids.input.text == "":
            self.ids.efficiency_answer.text = "Please fill in variables correctly"
        else:
            ouput = float(ouput)
            input = float(input)
            calc_answer = (ouput / input)*100
            self.ids.efficiency_answer.text = str(calc_answer) 
#.................................................
#functions for the Energy screen
class EnergyScreen(Screen):
    def backwards(self):
        self.manager.transition.direction="right"
        self.manager.current = "main_screen"
    def potential(self):
        self.manager.current = "potential_screen"
    def kinetic(self):
        self.manager.current = "kinetic_screen"
    def thermal(self):
        self.manager.current = "thermal_screen"
#.................................................
#functions for the potential screen
class PotentialScreen(Screen):
    def backwards3(self):
        self.manager.transition.direction="right"
        self.manager.current = "energy_screen"
    def get_potential_answer(self,mass,height):
        if self.ids.mass.text == "" or self.ids.height.text == "":
            self.ids.potential_answer.text = "Please fill in variables correctly"        
        else:
            mass = float(mass)
            height = float(height)
            calc_answer = (mass*9.81*height)
            self.ids.potential_answer.text = str(calc_answer) 
#.................................................
#functions for the kinetic screen
class KineticScreen(Screen):
    def backwards3(self):
        self.manager.transition.direction="right"
        self.manager.current = "energy_screen"
    def get_kinetic_answer(self,mass,velocity):
        if self.ids.mass.text == "" or self.ids.velocity.text == "":
            self.ids.kinetic_answer.text = "Please fill in variables correctly"        
        else:
            mass = float(mass)
            velocity = float(velocity)
            calc_answer = (0.5*mass*(velocity*velocity))
            self.ids.kinetic_answer.text = str(calc_answer) 
#.................................................
#functions for the thermal screen
class ThermalScreen(Screen):
    def backwards3(self):
        self.manager.transition.direction="right"
        self.manager.current = "energy_screen"
    def get_thermal_answer(self,mass,shc,t1,t2):
        if self.ids.mass.text == "" or self.ids.shc.text == "" or self.ids.t1.text == "" or self.ids.t2.text == "":
            self.ids.thermal_answer.text = "Please fill in variables correctly"
        else:
            mass = float(mass)
            shc = float(shc)
            t1 = float(t1)
            t2 = float(t2)
            calc_answer = (mass*shc*(t2-t1))
            self.ids.thermal_answer.text = str(calc_answer) 
#.................................................
#functions for the fluid screen
class FluidScreen(Screen):
    def backwards(self):
        self.manager.transition.direction="right"
        self.manager.current = "main_screen"
    def pressure(self):
        self.manager.current = "pressure_screen"
    def charleslaw(self):
        self.manager.current = "charleslaw_screen"
    def gllaw(self):
        self.manager.current = "gllaw_screen"
    def boyleslaw(self):
        self.manager.current = "boyleslaw_screen"
    def flowrate(self):
        self.manager.current = "flowrate_screen"
    def areavsvelocity(self):
        self.manager.current = "areavsvelocity_screen"
    def horsepower(self):
        self.manager.current = "horsepower_screen"


#.................................................
#functions for the absolute pressure screen
class PressureScreen(Screen):
    def backwards4(self):
        self.manager.transition.direction="right"
        self.manager.current = "fluid_screen"
    def get_pressure_answer(self,force,area):
        if self.ids.force.text == "" or self.ids.area.text == "":
            self.ids.pressure_answer.text = "Please fill in variables correctly"
        else:
            force = float(force)
            area = float(area)
            calc_answer = (force/area)
            self.ids.pressure_answer.text = str(calc_answer) 
#.................................................
#functions for the Charle's Law screen
class CharlesLawScreen(Screen):
    def backwards4(self):
        self.manager.transition.direction="right"
        self.manager.current = "fluid_screen"
    def get_charleslaw_answer(self,initial_temperature,final_temperature,final_velocity):
        if self.ids.initial_temperature.text == "" or self.ids.final_temperature.text == "" or self.ids.final_velocity.text == "":
            self.ids.charleslaw_answer.text = "Please fill in variables correctly"        
        else:
            initial_temperature = float(initial_temperature)
            final_temperature = float(final_temperature)
            final_velocity = float(final_velocity)        
            calc_answer = ((final_velocity/final_temperature)*initial_temperature)
            self.ids.charleslaw_answer.text = str(calc_answer) 
#.................................................
#functions for the Guy-Lussanc's Law screen
class GLLawScreen(Screen):
    def backwards4(self):
        self.manager.transition.direction="right"
        self.manager.current = "fluid_screen"
    def get_gllaw_answer(self,initial_temperature,final_temperature,final_pressure):
        if self.ids.initial_temperature.text == "" or self.ids.final_temperature.text == "" or self.ids.final_pressure.text == "":
            self.ids.gllaw_answer.text = "Please fill in variables correctly"   
        else:
            initial_temperature = float(initial_temperature)
            final_temperature = float(final_temperature)
            final_pressure = float(final_pressure)        
            calc_answer = ((final_pressure/final_temperature)*initial_temperature)
            self.ids.gllaw_answer.text = str(calc_answer) 
#.................................................
#functions for the Boyle's Law screen
class BoylesLawScreen(Screen):
    def backwards4(self):
        self.manager.transition.direction="right"
        self.manager.current = "fluid_screen"
    def get_boyleslaw_answer(self,initial_velocity,final_velocity,final_pressure):
        if self.ids.initial_velocity.text == "" or self.ids.final_velocity.text == "" or self.ids.final_pressure.text == "":
            self.ids.boyleslaw_answer.text = "Please fill in variables correctly"           
        else:  
            initial_velocity = float(initial_velocity)
            final_velocity = float(final_velocity)
            final_pressure = float(final_pressure)        
            calc_answer = ((final_pressure*final_velocity)*initial_velocity)
            self.ids.boyleslaw_answer.text = str(calc_answer) 
#.................................................
#functions for the flow rate screen
class FlowRateScreen(Screen):
    def backwards4(self):
        self.manager.transition.direction="right"
        self.manager.current = "fluid_screen"
    def get_flowrate_answer(self,area,velocity):
        if self.ids.area.text == "" or self.ids.velocity.text == "":
            self.ids.flowrate_answer.text = "Please fill in variables correctly"   
        else:
            area = float(area)
            velocity = float(velocity)
            calc_answer = (area*velocity)
            self.ids.flowrate_answer.text = str(calc_answer) 
#.................................................
#functions for the area vs velocity screen
class AreavsVelocityScreen(Screen):
    def backwards4(self):
        self.manager.transition.direction="right"
        self.manager.current = "fluid_screen"
    def get_areavsvelocity_answer(self,initial_velocity,final_velocity,final_area):
        if self.ids.initial_velocity.text == "" or self.ids.final_velocity.text == "" or self.ids.final_area.text == "":
            self.ids.areavsvelocity_answer.text = "Please fill in variables correctly"   
        else: 
            initial_velocity = float(initial_velocity)
            final_velocity = float(final_velocity)
            final_area = float(final_area)        
            calc_answer = ((final_area*final_velocity)/initial_velocity)
            self.ids.areavsvelocity_answer.text = str(calc_answer) 
#.................................................
#functions for the horse power screen
class HorsePowerScreen(Screen):
    def backwards4(self):
        self.manager.transition.direction="right"
        self.manager.current = "fluid_screen"
    def get_horsepower_answer(self,flowrate,pressure,efficiency):
        if self.ids.flowrate.text == "" or self.ids.pressure.text == "" or self.ids.efficiency.text == "":
            self.ids.horsepower_answer.text = "Please fill in variables correctly"   
        else:
            flowrate = float(flowrate)
            pressure = float(pressure)
            efficiency = float(efficiency)        
            calc_answer = ((flowrate*pressure)/(1714*efficiency))
            self.ids.horsepower_answer.text = str(calc_answer) 
#.................................................
#functions for the electricity screen
class ElectricityScreen(Screen):
    def backwards(self):
        self.manager.transition.direction="right"
        self.manager.current = "main_screen"
    def voltage(self):
        self.manager.current = "voltage_screen"
    def electric_power(self):
        self.manager.current = "electric_power_screen"

#.................................................
#functions for the voltage screen
class VoltageScreen(Screen):
    def backwards5(self):
        self.manager.transition.direction="right"
        self.manager.current = "electricity_screen"
    def get_voltage_answer(self,current,resistance):
        if self.ids.current.text == "" or self.ids.resistance.text == "":
            self.ids.voltage_answer.text = "Please fill in variables correctly"           
        else:
            current = float(current)
            resistance = float(resistance)
            calc_answer = (current*resistance)
            self.ids.voltage_answer.text = str(calc_answer) 
#.................................................
#functions for the electric power screen
class ElectricPowerScreen(Screen):
    def backwards5(self):
        self.manager.transition.direction="right"
        self.manager.current = "electricity_screen"
    def get_electric_power_answer(self,current,voltage):
        if self.ids.current.text == "" or self.ids.voltage.text == "":
            self.ids.electric_power_answer.text = "Please fill in variables correctly"   
        else:
            current = float(current)
            voltage = float(voltage)
            calc_answer = (current*voltage)
            self.ids.electric_power_answer.text = str(calc_answer) 
#...............................................
#..............................................

# Defines Root widget to make it work
class RootWidget(ScreenManager):
    pass

# Creates the application
class MainApp(App):
    def build(self):
        return RootWidget()

# Runs application
if __name__ == "__main__":
    MainApp().run()
