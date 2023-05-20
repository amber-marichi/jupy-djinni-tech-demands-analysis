import aiohttp
import asyncio
import re
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


async def parse_vacancy(soup: BeautifulSoup) -> Vacancy:
    exp = (
        soup.select_one(".list-jobs__details__info")
        .find(string=re.compile(r"досвіду")).split()[1]
    )
    if exp.isnumeric():
        exp = int(exp)
    else:
        exp = 0

    info = soup.select_one(".text-date").text.split()
    replies = info.pop()
    views = info.pop()
    if info[0] == "сьогодні":
        real_date = datetime.now()
    elif info[0] == "вчора":
        real_date = datetime.now() - timedelta(days=1)
    else:
        real_date = datetime.strptime(" ".join(info), "%d %B")

    return Vacancy(
        title=(
            soup.select_one(".list-jobs__title").text
            .strip().replace("\n", " ")
        ),
        posted=real_date.date(),
        experience=exp,
        views=int(views),
        replies=int(replies),
        description=soup.select_one(".text-card").text.strip(),
        link=urljoin(
            config.BASE_URL,
            soup.select_one(".profile[href]")["href"]
        )
    )


async def parse_page(soup: BeautifulSoup) -> list[Vacancy]:
    vacancies = soup.select(".list-jobs__item")
    return await asyncio.gather(
        *[parse_vacancy(vacancy) for vacancy in vacancies]
    )
