# -*- coding: utf-8 -*-
from gi.repository import Gtk, Gdk, GdkPixbuf
import os
import sys
from ..CSVHandler import CSVFile

"""
Reminder : how the Builder works
--------------------------------
The Gtk.Builder class offers you the opportunity to design user interfaces without writing a single line of code. This is possible through describing the interface by a XML file (done via Glade) and then loading the XML description at runtime and create the objects automatically, which the Builder class does for you.
"""
# Trick to allow relative paths
#file_path = os.path.abspath(os.path.dirname(sys.argv[0]))
#os.chdir(file_path)

builder = Gtk.Builder()
builder.add_from_file("theforce/GUI/main.glade")

# Main window
main_window = builder.get_object("main_window")
# the icon list
small_icon = GdkPixbuf.Pixbuf.new_from_file("theforce/GUI/icons/yoda_32.png")
medium_icon = GdkPixbuf.Pixbuf.new_from_file("theforce/GUI/icons/yoda_64.png")
large_icon = GdkPixbuf.Pixbuf.new_from_file("theforce/GUI/icons/yoda_128.png")
main_window.set_icon_list([small_icon, medium_icon, large_icon])

# Display area
scrolledwindow_display = builder.get_object("scrolledwindow_display")

# Information panel
default_info_label = builder.get_object("default_info_label")

# Signal handlers
class Signal_Handlers:
	def on_main_window_delete_event(self, *args):
		Gtk.main_quit(*args)
		
	def on_filechooserbutton_file_set(self, widget):
		csv_file = CSVFile(widget.get_filename())
		
		# Create a grid representation of the csv
		grid = Gtk.Grid()
		grid.set_column_spacing(10)
		scrolledwindow_display.add_with_viewport(grid)
		
		for h in csv_file.headers:
			col_no = csv_file.headers.index(h)
			label_header = Gtk.Label()
			label_header.set_markup("<b>"+h+"</b>")
			grid.attach(label_header, left=col_no, top=0, width=1, height=1)
			row_no = 0
			for d in csv_file.data[h]:
				row_no += 1
				grid.attach(Gtk.Label(str(d)), left=col_no, top=row_no, width=1, height=1)
		scrolledwindow_display.show_all()
		
builder.connect_signals(Signal_Handlers())
main_window.show_all()

Gtk.main()
