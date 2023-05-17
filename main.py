#!/usr/bin/env python3
from dataclasses import astuple
from leantechniques_demo.request import get_photos
from textual.app import App, ComposeResult
from textual.containers import Container, Vertical, VerticalScroll
from textual.widgets import DataTable, Input, Button

HEADERS = ['ID', 'Album ID', 'Title', 'URL', 'Thumbnail URL']

class DisplayApp(App):
    '''Main application class'''
    CSS_PATH = 'layout.css'

    def compose(self) -> ComposeResult:
        with Container(id='app-grid'):
            with Vertical(id='left-pane'):
                yield Input(placeholder='Filter by ID', classes='box', id='id')
                yield Input(placeholder='Filter by Album ID', classes='box', id='albumId')
                yield Input(placeholder='Filter by Title', classes='box', id='title')
                yield Button('Load Data', id='load_data')
            with VerticalScroll(id='right-pane'):
                yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*HEADERS)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'load_data':
            request_filter_inputs = self.query(Input).exclude('#title')
            local_filter_input = self.query_one('#title').value
            params = {i.id: i.value for i in request_filter_inputs if i.value}
            data = [astuple(i) for i in get_photos(**params) if local_filter_input in i.title]
            table = self.query_one(DataTable)
            table.clear()
            table.add_rows(data)

if __name__ == "__main__":
    app = DisplayApp()
    app.run()