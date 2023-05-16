from dataclasses import dataclass
from urllib.parse import urlparse

@dataclass
class Album:
    '''Data container for the photo album structure.'''
    albumId: int
    id: int
    title: str
    url: str
    thumbnailUrl: str

    def validate(self):
        if not isinstance(self.albumId, int):
            raise TypeError(f'albumId {self.albumId} is not an integer')
        if not isinstance(self.id, int):
            raise TypeError(f'id {self.id} is not an integer')
        if not isinstance(self.title, str):
            raise TypeError(f'title {self.title} is not a string')
        if not urlparse(self.url).netloc or not urlparse(self.url).scheme:
            raise ValueError(f'url {self.url} appears to be malformed')
        if not urlparse(self.thumbnailUrl).netloc or not urlparse(self.thumbnailUrl).scheme:
            raise ValueError(f'thumbnailUrl {self.thumbnailUrl} appears to be malformed')
        return True