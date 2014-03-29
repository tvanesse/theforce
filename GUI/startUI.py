# -*- coding: utf-8 -*-
from gi.repository import Gtk

"""
Reminder : how the Builder works
--------------------------------
The Gtk.Builder class offers you the opportunity to design user interfaces without writing a single line of code. This is possible through describing the interface by a XML file (done via Glade) and then loading the XML description at runtime and create the objects automatically, which the Builder class does for you.
"""
builder = Gtk.Builder()
builder.add_from_file("test.glade")

# Main window
window = builder.get_object("main_window")
window.show_all()

# Signal handlers
class Signal_Handlers:
	def on_main_window_delete_event(self, *args):
		Gtk.main_quit(*args)
		
builder.connect_signals(Signal_Handlers())

Gtk.main()
