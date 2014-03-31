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

# -----------------
# Filters iconview
# -----------------
filters_iconview = builder.get_object("filters_iconview")
filters_liststore = builder.get_object("filters_liststore")
filters_iconview.set_pixbuf_column(1)
filters_iconview.set_text_column(0)
# The different filters
filters_liststore.append(["Field selector", Gtk.IconTheme.get_default().load_icon("gtk-copy", 32, 0)])
# Drag and drop behaviour. This is the source.
filters_iconview.enable_model_drag_source(Gdk.ModifierType.BUTTON1_MASK, [], Gdk.DragAction.COPY)

# -----------------
# Workflow grid
# -----------------
workflow_grid = builder.get_object("workflow_grid")
workflow_grid.drag_dest_set(Gtk.DestDefaults.ALL, [], Gdk.DragAction.COPY)
first_frame_label = builder.get_object("first_frame_label")
first_frame_label.drag_dest_set(Gtk.DestDefaults.ALL, [], Gdk.DragAction.COPY)


# Signal handlers
class Signal_Handlers:
	def on_main_window_delete_event(self, *args):
		Gtk.main_quit(*args)
		
	def on_filechooserbutton_file_set(self, widget):
		# Destroy the yoda head
		builder.get_object("yoda_viewport").destroy()
		
		# Load the file
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
		
	def on_filters_iconview_drag_begin(self, widget, drag_context):
		print("Drag started.")
		
	def on_filters_iconview_drag_data_get(self, widget, drag_context):
		print("Drag launched.")
		
	def on_workflow_drag_data_received(self, widget, drag_context, x,y, data,info, time):
		print("Drop")
		
	def on_workflow_drag_motion(self, widget, drag_context):
		print("Fly me to the moon")
		
builder.connect_signals(Signal_Handlers())
main_window.show_all()

Gtk.main()
