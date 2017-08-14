# -*- coding: utf-8 -*-
__author__ = 'Johnny'

from flask import Blueprint,request,g
from ..services import customer
from passlib.apps import custom_app_context as pwd_context
from ..tools import helper
from .import route,route_nl

bp=Blueprint('customer',__name__,url_prefix='/customer')


@route(bp,'/')
def list():
    """
        查询，返回全部
    """
    return customer.all()

@route(bp,'/<customer_id>/quota/')
def get_customer_quota(customer_id):
    """
    根据用户获得额度
    :return:
    """
    return customer.get_or_404(customer_id).quotaes


@route(bp,'/<customer_id>')
def show(customer_id):
    """
        查找单个
    """
    return customer.get_or_404(customer_id)

@route(bp,'/<customer_id>/quotas')
def quotas(customer_id):
    """
    查找每个用户的额度
    :param customer_id:
    :return:
    """
    return customer.get_or_404(customer_id).quotaes

"""页面组成字典或者json"""
@route_nl(bp,'/',methods=['POST'])
def new():
    request_json=dict(**request.json)
    _cutomer=dict(request_json.get('customer'))

    _password=_cutomer['password']
    password=pwd_context.encrypt(_password)
    _cutomer['password']=password

    request_json['customer']=_cutomer

    # data={
    #     "customer":{
    #         "real_name":customer['real_name'],
    #         "identification_number":customer['identification_number'],
    #         "phone":customer['phone'],
    #         "password":customer['password'],
    #     }
    # }

    g.customer=customer.create(**request_json)

    token=g.customer.generate_auth_token()
    return {"customer":g.customer,
            "token":token.decode('ascii')}

@route(bp,'/<customer_id>',methods=['PUT'])
def update(customer_id):
    return customer.update(customer.get_or_404(customer_id),**request.json)

@route(bp,'/<customer_id>',methods=['DELETE'])
def delete(customer_id):
    customer.delete(customer.get_or_404(customer_id))
    return None,204



