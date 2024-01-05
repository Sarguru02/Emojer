import gi
gi.require_version('Gtk', '3.0')
from test import searcher
from gi.repository import Gtk, Gdk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Search Window")
        self.set_border_width(10)

        # Create a vertical box to hold the input box and the search button
        vbox = Gtk.VBox(spacing=6)
        self.add(vbox)

        # Create an input box (Gtk.Entry)
        self.input_entry = Gtk.Entry()
        self.input_entry.set_placeholder_text("Type something...")
        self.input_entry.connect("activate", self.on_search_button_clicked)
        vbox.pack_start(self.input_entry, False, False, 0)

        # Create a Search button
        search_button = Gtk.Button(label="Search")
        search_button.connect("clicked", self.on_search_button_clicked)
        vbox.pack_start(search_button, False, False, 0)

        # Container for result buttons (changed to Gtk.HBox)
        self.result_button_box = Gtk.HBox(spacing=6)
        vbox.pack_start(self.result_button_box, False, False, 0)

    def on_search_button_clicked(self, widget):
        # Clear existing result buttons
        for child in self.result_button_box.get_children():
            self.result_button_box.remove(child)

        search_text = self.input_entry.get_text()
        search_results = searcher(search_text)

        #create buttons for each result
        for result in search_results:
            button = Gtk.Button(label=result)
            button.connect("clicked", self.on_result_button_clicked)
            self.result_button_box.pack_start(button, False, False, 0)
        # show the buttons
        self.result_button_box.show_all()

    def on_result_button_clicked(self, widget):
        label_text = widget.get_label()

        # Copy the label text to the clipboard
        clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        clipboard.set_text(label_text, -1)
        clipboard.store()
        print("Copied to clipboard")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()
