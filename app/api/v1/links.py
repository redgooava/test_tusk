import csv

from fastapi import APIRouter
import requests
from fpdf import FPDF

from app.schemas import AppendRequest, AppendResponse, FindRequest, FindResponse

api_v1_links_router = APIRouter()


@api_v1_links_router.post("/", response_model=AppendResponse)
async def post_links(data: AppendRequest):
    with open('app/data/data.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        number_of_str = len(list(reader))

    resp_links = check_links(data.links)

    with open('app/data/data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data.links)

    return AppendResponse(
        links=resp_links,
        links_num=number_of_str
    )

@api_v1_links_router.post("/pdf")
async def get_pdf(data: FindRequest):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    with open('app/data/data.csv', 'r', newline='') as f:
        links = list(csv.reader(f))
    for search_str_number in data.links_list:
        pdf.cell(0, 10, str(check_links(links[search_str_number])), 0, 1, 'C')
    pdf.output("simple.pdf")


def check_links(links):
    resp_links = dict()
    for link in links:
        try:
            req = requests.get(link, timeout=5)
            if req.status_code >= 500:
                resp_links[link] = 'not_available'
            else:
                resp_links[link] = 'available'
        except requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout:
            resp_links[link] = 'not_available'
    return resp_links