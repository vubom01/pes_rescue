import csv
import datetime
import logging
from typing import Optional

import cloudinary
from fastapi import APIRouter, Depends, HTTPException

from app.helpers.login_manager import PermissionRequired
from app.schemas.sche_sponsor import DonateDetailRequest
from app.services.srv_sponsor import SponsorService

logger = logging.getLogger()
router = APIRouter()

@router.post('', dependencies=[Depends(PermissionRequired('admin'))])
def upsert_donate_detail(req: DonateDetailRequest):
    if req.id is None:
        if req.sponsor_id is None:
            raise HTTPException(status_code=400, detail='sponsor_id khong duoc de trong')
        if req.account_number is None:
            raise HTTPException(status_code=400, detail='account_number khong duoc de trong')
        if req.transaction_code is None:
            raise HTTPException(status_code=400, detail='transaction_code khong duoc de trong')
        if req.donations is None:
            raise HTTPException(status_code=400, detail='donations khong duoc de trong')

        sponsor = SponsorService.get_sponsor(id=req.sponsor_id)
        if sponsor is None:
            raise HTTPException(status_code=400, detail='Sponsor not found')

        donate_detail = SponsorService.is_exist_donate_detail(transaction_code=req.transaction_code)
        if donate_detail:
            raise HTTPException(status_code=400, detail='Donate detail is already exist')

        SponsorService.create_donate_detail(data=req)
        return {
            'id': SponsorService.is_exist_donate_detail(transaction_code=req.transaction_code).get('id')
        }

    else:
        donate_detail = SponsorService.get_donate_detail_by_id(id=req.id)
        if donate_detail is None:
            raise HTTPException(status_code=400, detail='Donate detail not found')

        if req.transaction_code:
            if req.transaction_code != donate_detail.get('transaction_code'):
                donate_detail = SponsorService.is_exist_donate_detail(transaction_code=req.transaction_code)
                if donate_detail:
                    raise HTTPException(status_code=400, detail='Donate detail is already exist')
        else:
            req.transaction_code = donate_detail.get('transaction_code')

        if req.sponsor_id:
            sponsor = SponsorService.get_sponsor(id=req.sponsor_id)
            if sponsor is None:
                raise HTTPException(status_code=400, detail='Sponsor not found')
        else:
            req.sponsor_id = donate_detail.get('sponsor_id')

        if req.account_number is None:
            req.account_number = donate_detail.get('account_number')
        if req.donations is None:
            req.donations = donate_detail.get('donations')

        SponsorService.update_donate_detail(data=req)
        return {
            'id': req.id
        }

@router.get('', dependencies=[Depends(PermissionRequired('admin'))])
def get_list_donate_detail(start_at: Optional[datetime.date] = None, end_at: Optional[datetime.date] = None):
    data = SponsorService.get_list_donate_detail(start_at=start_at, end_at=end_at)
    fields = ['id', 'created_at', 'sponsor_id', 'full_name', 'email', 'phone_number', 'account_number',
              'transaction_code', 'donations']
    file = open('donate_detail.csv', "w", newline="\n")
    writer = csv.writer(file, delimiter=",")

    writer.writerow(fields)
    for field in data:
        values = list(field.values())
        values[1] = datetime.date.strftime(values[1], "%d-%m-%Y")
        writer.writerow(values)
    file.close()

    folder = "donate_detail/" + str(start_at.year) + "/" + str(start_at.month)
    name = "donate_detail_T" + str(start_at.month)
    result = cloudinary.uploader.upload('donate_detail.csv', folder=folder, public_id=name,
                                        resource_type='raw')
    url = result.get('url')
    return {
        'url': url
    }


