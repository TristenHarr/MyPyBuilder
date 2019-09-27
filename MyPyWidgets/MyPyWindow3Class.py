import tkinter as tk


class MyPyWindow(tk.Frame):

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.type = kwargs['type']
        self.base_location = kwargs['base_location']
        if 'title' in kwargs.keys():
            self.title = kwargs['title']
        self.id = kwargs['id']
        self.owner = kwargs['owner']
        self.containers = {}
        self.master = kwargs['master']
        self.types = {'frame': [lambda x: x, self.master],
                      'toplevel': [tk.Toplevel, self.master],
                      'root': [tk.Tk, None]}
        self.app = self.types[self.type][0](self.types[self.type][1])
        self.screen_height = None
        self.screen_width = None
        self.sharrre_intt = lambda x: x[10] + x[3] + x[8] + x[0] + x[11] + x[6] + x[9] + x[7] + x[1] + x[2] + x[4] + x[
            5]
        super().__init__(master=self.app)
        if self.type is not 'frame':
            self.app.attributes('-alpha', 0)
            self.dragger = self.app
        else:
            self.dragger = None
            self.canvas = None
            self.view_window = None
            self.scroll_bary = None
            self.scroll_barx = None
        if 'config' not in kwargs.keys():
            kwargs['config'] = {}
        self.configure(**kwargs['config'])
        self.root = self.find_root(self.app)
        self.screen_height = self.root.winfo_screenheight()
        self.screen_width = self.root.winfo_screenwidth()
        tk.Grid.rowconfigure(self.app, 0, weight=1)
        tk.Grid.columnconfigure(self.app, 0, weight=1)
        for i in range(self.base_location['rowspan']):
            self.grid_rowconfigure(i, minsize=1)
            tk.Grid.rowconfigure(self, i, weight=1)
        for i in range(self.base_location['columnspan']):
            self.grid_columnconfigure(i, minsize=1)
            tk.Grid.columnconfigure(self, i, weight=1)
        self.row_offset = 0
        self.column_offset = 0
        if 'row_offset' in kwargs.keys():
            self.row_offset = kwargs['row_offset']
        if 'column_offset' in kwargs.keys():
            self.column_offset = kwargs['column_offset']

    def find_root(self, current):
        if str(current) is not '.':
            return self.find_root(current.master)
        else:
            return current

    def setup(self):
        if self.type is not 'frame':
            self.app.title(self.title)
            self.app.protocol('WM_DELETE_WINDOW', self.leave)
            h = int(self.screen_height - self.base_location['rowspan']) // 2
            w = int(self.screen_width - self.base_location['columnspan']) // 2
            self.app.geometry('+{}+{}'.format(w + self.column_offset, h + self.row_offset))
            self.app.attributes('-alpha', 1)
        self.grid(**self.base_location)
        self.update_idletasks()
        self.frame_builder()

    def run(self):
        self.mainloop()

    def add_frame(self, **kwargs):
        if kwargs['id'] in self.containers.keys():
            self.containers[kwargs['id']].destroy()
            garbage = self.containers.pop(kwargs['id'])
            del garbage
        kwargs['owner'] = self.owner
        kwargs['type'] = 'frame'
        if kwargs['scroll']['horizontal'] or kwargs['scroll']['vertical']:
            canvas = None
            scroll_barx = None
            scroll_bary = None
            canvas = tk.Canvas(self, bg='white')
            kwargs['master'] = canvas
            self.containers[kwargs['id']] = MyPyWindow(**kwargs)
            self.containers[kwargs['id']].setup()
            canvas.create_window((0, 0), window=self.containers[kwargs['id']], anchor='nw')
            if kwargs['scroll']['horizontal']:
                scroll_barx = tk.Scrollbar(self, orient='horizontal', command=canvas.xview)
                canvas.configure(xscrollcommand=scroll_barx.set)
            if kwargs['scroll']['vertical']:
                scroll_bary = tk.Scrollbar(self, orient='vertical', command=canvas.yview)
                canvas.configure(yscrollcommand=scroll_bary.set)
            self.containers[kwargs['id']].bind('<Configure>', lambda event, _canvas=canvas: self.scroller(_canvas))
            if kwargs['scroll']['horizontal'] and kwargs['scroll']['vertical']:
                kwargs['scroll_window_size']['rowspan'] -= 20
                kwargs['scroll_window_size']['columnspan'] -= 20
                scroll_barx.grid(row=kwargs['scroll_window_size']['row'] + kwargs['scroll_window_size']['rowspan'],
                                 rowspan=20,
                                 column=kwargs['scroll_window_size']['column'],
                                 columnspan=kwargs['scroll_window_size']['columnspan'],
                                 sticky='NWE')
                scroll_bary.grid(
                    row=kwargs['scroll_window_size']['row'],
                    rowspan=kwargs['scroll_window_size']['rowspan'],
                    column=kwargs['scroll_window_size']['column'] + kwargs['scroll_window_size']['columnspan'],
                    columnspan=20,
                    sticky='NSW'
                )
            elif kwargs['scroll']['horizontal']:
                kwargs['scroll_window_size']['rowspan'] -= 20
                scroll_barx.grid(row=kwargs['scroll_window_size']['row'] + kwargs['scroll_window_size']['rowspan'],
                                 rowspan=20,
                                 column=kwargs['scroll_window_size']['column'],
                                 columnspan=kwargs['scroll_window_size']['columnspan'],
                                 sticky='NWE')
            elif kwargs['scroll']['vertical']:
                kwargs['scroll_window_size']['columnspan'] -= 20
                scroll_bary.grid(
                    row=kwargs['scroll_window_size']['row'],
                    rowspan=kwargs['scroll_window_size']['rowspan'],
                    column=kwargs['scroll_window_size']['column'] + kwargs['scroll_window_size']['columnspan'],
                    columnspan=20,
                    sticky='NSW'
                )
            canvas.grid(**kwargs['scroll_window_size'])
        else:
            kwargs['master'] = self
            self.containers[kwargs['id']] = MyPyWindow(**kwargs)
            self.containers[kwargs['id']].setup()
            self.containers[kwargs['id']].configure({'bg': 'green'})
        self.containers[kwargs['id']].dragger = self.containers[kwargs['id']]

    def add_widget(self, **kwargs):
        if kwargs['id'] in self.containers.keys():
            self.containers[kwargs['id']].destroy()
            garbage = self.containers.pop(kwargs['id'])
            del garbage
        self.containers[kwargs['id']] = kwargs['widget'](*[self, *kwargs['args']])
        self.containers[kwargs['id']].set_base_location(kwargs['location'])
        if 'config' in kwargs.keys():
            self.containers[kwargs['id']].configure(kwargs['config'])
        self.containers[kwargs['id']].show_widget()

    def add_toplevel(self, **kwargs):
        if kwargs['id'] in self.containers.keys():
            self.containers[kwargs['id']].destroy()
            garbage = self.containers.pop(kwargs['id'])
            del garbage
        kwargs['owner'] = self.owner
        kwargs['type'] = 'toplevel'
        kwargs['master'] = self
        self.containers[kwargs['id']] = MyPyWindow(**kwargs)
        self.containers[kwargs['id']].setup()

    def destroy_item(self, item):
        if item in self.containers.keys():
            garbage = self.containers.pop(item)
            garbage.destroy()
            del garbage

    def add_item(self, wid, item):
        self.containers[wid] = item

    def frame_builder(self):
        """
        Override me
        :return: None
        """
        pass

    # IN DEV
    def scroller(self, canvas):
        canvas.configure(scrollregion=canvas.bbox('all'), width=1, height=1)

    # END DEV

    def leave(self):
        self.app.destroy()
