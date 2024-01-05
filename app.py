import gi, emoji
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk


l = ["Hello", "World", ]
items = [key for key in emoji.EMOJI_DATA.keys()]


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello GTK")
        self.set_border_width(10)

        # Create a scrolled window to enable vertical scrolling
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.add(scrolled_window)

        # Create a vertical box to hold the horizontal boxes
        vbox_outer = Gtk.VBox(spacing=6)
        scrolled_window.add(vbox_outer)

        # Create horizontal boxes to hold buttons
        hbox_list = []
        buttons_per_box = 10  # You can adjust this value based on your preference

        for i in range(0, len(items), buttons_per_box):
            hbox = Gtk.HBox(spacing=6)
            for item in items[i:i+buttons_per_box]:
                button = Gtk.Button(label=str(item))
                button.set_size_request(100, 30)
                button.connect("clicked", self.on_button_clicked)
                hbox.pack_start(button, True, True, 0)
            hbox_list.append(hbox)

        # Add the horizontal boxes to the vertical box
        for hbox in hbox_list:
            vbox_outer.pack_start(hbox, False, False, 0)

    def on_button_clicked(self, widget):
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
