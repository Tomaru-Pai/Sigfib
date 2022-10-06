""" Informations:
    ‾‾‾‾‾‾‾‾‾‾‾‾
    Diploma Thesis:     Sigfib
    Authors:            Thomas Pail, Maximilian Hutter
    Assistant Teacher:  Prof. DI. Rudolf Schamberger
    School:             HTBL u. VA BULME
    Year of graduation: 2023
 
    Sigfib -> Import of Gerber Files into Blender
    ┃┃┃┃┃┃
    ┃┃┃┃┃┗━━► Blender
    ┃┃┃┃┗━━━► In
    ┃┃┃┗━━━━► Files
    ┃┃┗━━━━━► Gerber
    ┃┃        of
    ┃┗━━━━━━► Import
    ┗━━━━━━━► Simple

    Description: 
    ‾‾‾‾‾‾‾‾‾‾‾
    Sigfib is a Plugin for the software Blender which allows the user to easily import 
    .gbr (Gerber) Files form the PCB Design Software Altium Designer. 
    The user has full controll over color customization, material properties etc. 
    With the footprints of the .gbr file the plugin can place the correct 3D models of the 
    packages inside a collection in blender. The PCB can be, with the right chosen integrated settings 
    instandly rendered. For further presentation it also features cinematic animation tools.
    If a custom model needs to be imported, then it is required to either upload the model to your 
    local footprint database or to one-time import it inside of the Plugin itself to ensure full 
    functionality with the plugin. 

    Features:
    ‾‾‾‾‾‾‾‾
    ┗━━► Import Gerber:
    ┗━━► Import Settings:
    ┗━━► Cinematic Tools:
    ┗━━► Library Database:

    Version Documentation: 
    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    ┗━━► Ver. 0.0: Description, UI classes
    ┗━━► Ver. 0.1: 
"""
# Displayes important informations for the user about the Plugin
# such as: Name, Authors, Plugin Version, Tested Blender Version afm. 
bl_info = {
    "name": "",
    "author": "",
    "version": (1, 0),
    "blender": (2, 80, 3),
    "location": "",
    "description": "",
    "warning": "",
    "wiki_url": "",
    "category": "",
}

# Import of Blender API Module
import bpy
from bpy.types import Operator
from bpy_extras.io_utils import ImportHelper

from bpy.props import StringProperty, BoolProperty

# Modules by Sigfib Team

# Modules from other sources

# https://docs.blender.org/api/current/bpy.types.Panel.html
class Sigfib:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S i g f i b" # Spaces were added due to better readability in  the Blender UI
    bl_options = {"DEFAULT_CLOSED"}

# In the Widget several Modules can be added and will be shown like
# a dictionary list. These Modules represent the several functions.
class ImportGerber(Sigfib, bpy.types.Panel):
    bl_idname = "ImportGerber"
    bl_label = "Import Gerber"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Import of Gerber Files into Blender")

    # Import Window with dimension settings (1:1, 1:2, etc.)
    # Debug Window, where import feedback is displayed
    # E.g A Footprint is not recognised
    # E.g A Footprint could be colliding with two database inputs

class ImportSettings(Sigfib, bpy.types.Panel):
    bl_idname = "ImportSettings"
    bl_label = "Import Settings"

    def draw(self, context):
        layout = self.layout
        # layout.label(text="Setup colors, textures, material properties and names")

    # -> Button for default settings
    # -> Look at Eagle preview panel to observe needed color informations
    # -> Presetting for vias and pads with shiny texture
    # -> Box for Name entering: the imported file will be stored as a Collection

class CinematicTools(Sigfib, bpy.types.Panel):
    bl_idname = "CinematicTools"
    bl_label = "Cinematic Tools"

    def draw(self, context):
        layout = self.layout
        # layout.label(text="Scene lighting, exploded view, rotation")

class LibraryDatabase(Sigfib, bpy.types.Panel):
    bl_idname = "LibraryDatabase"
    bl_label = "Library Database"
    
    def draw(self, context):
        layout = self.layout

    # Get special objects from the used library or add missing Models 

classes = {
    ImportGerber,
    ImportSettings,
    CinematicTools,
    LibraryDatabase
}

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__" :
    register()