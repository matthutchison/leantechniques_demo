#!/usr/bin/env python3
from leantechniques_demo.request import get_photos
from textual.app import App, ComposeResult
from textual.containers import Container, Vertical, VerticalScroll
from textual.reactive import reactive
from textual.widgets import DataTable, Input, Button, Label

class ReactiveLabel(Label):
    '''Label widget with reactive text'''
    text = reactive('', layout=True)

    def render(self) -> str:
        return f'{self.text}'

class DisplayApp(App):
    '''Main application class'''
    CSS_PATH = 'layout.css'
    info = ReactiveLabel('default', id='info')

    def compose(self) -> ComposeResult:
        with Container(id='app-grid'):
            with Vertical(id='left-pane'):
                # UI element ids matter on the inputs, they're used as the query parameter name when accessing the API
                yield Input(placeholder='Filter by Photo ID', classes='box', id='id')
                yield Input(placeholder='Filter by Album ID', classes='box', id='albumId')
                yield Input(placeholder='Filter by Title', classes='box', id='title')
                yield Button('Load Data', id='load_data')
                yield self.info

            with VerticalScroll(id='right-pane'):
                yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns('Photo ID', 'Album ID', 'Title')

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'load_data':
            self.update_table()

    def update_table(self) -> None:
        try:
            request_filter_inputs = self.query(Input).exclude('#title')
            title_filter = self.query_one('#title').value
            params = {i.id: i.value for i in request_filter_inputs if i.value}
            data = [(i.id, i.albumId, i.title) for i in get_photos(**params) if title_filter in i.title]
            table = self.query_one(DataTable)
            table.clear()
            table.add_rows(data)
            self.info.text = f'({len(data)}) rows matching criteria'
        except Exception as e:
            self.info.text = f'An error occurred while fetching records.'


if __name__ == "__main__":
    app = DisplayApp()
    app.run()