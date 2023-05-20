from bs4 import BeautifulSoup
from urllib.parse import urljoin
from dataclasses import dataclass, astuple, fields
from datetime import datetime, date, timedelta

import config


@dataclass
class Vacancy:
    title: str
    posted: date
    experience: int
    views: int
    replies: int
    description: str
    link: str
