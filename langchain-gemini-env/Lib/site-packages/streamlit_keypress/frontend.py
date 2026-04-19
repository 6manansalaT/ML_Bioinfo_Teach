import os
import streamlit.components.v1 as components

parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "component")
_component_func = components.declare_component("key_press_listener", path=build_dir)

def key_press_events():
    """
    Create a component that captures keyboard events.
    
    Returns:
        The key that was pressed
    """
    value = _component_func()
    return value