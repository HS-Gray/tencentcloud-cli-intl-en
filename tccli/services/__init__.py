# -*- coding: utf-8 -*-
import os
import imp


def action_caller(service):
    cur_path = os.path.dirname(os.path.abspath(__file__))
    fp, pathname, desc = imp.find_module(service, [cur_path])
    mod = imp.load_module("tccli.services." + service, fp, pathname, desc)
    return mod.action_caller


SERVICE_VERSIONS = {
    "antiddos": [
        "2020-03-09"
    ],
    "apigateway": [
        "2018-08-08"
    ],
    "autoscaling": [
        "2018-04-19"
    ],
    "batch": [
        "2017-03-12"
    ],
    "billing": [
        "2018-07-09"
    ],
    "cam": [
        "2019-01-16"
    ],
    "cbs": [
        "2017-03-12"
    ],
    "cdb": [
        "2017-03-20"
    ],
    "cdn": [
        "2018-06-06"
    ],
    "cfs": [
        "2019-07-19"
    ],
    "chdfs": [
        "2020-11-12"
    ],
    "ckafka": [
        "2019-08-19"
    ],
    "clb": [
        "2018-03-17"
    ],
    "cloudaudit": [
        "2019-03-19"
    ],
    "cls": [
        "2020-10-16"
    ],
    "cmq": [
        "2019-03-04"
    ],
    "cvm": [
        "2017-03-12"
    ],
    "cynosdb": [
        "2019-01-07"
    ],
    "dayu": [
        "2018-07-09"
    ],
    "dbbrain": [
        "2021-05-27",
        "2019-10-16"
    ],
    "dc": [
        "2018-04-10"
    ],
    "dcdb": [
        "2018-04-11"
    ],
    "dms": [
        "2020-08-19"
    ],
    "dts": [
        "2018-03-30"
    ],
    "eb": [
        "2021-04-16"
    ],
    "ecdn": [
        "2019-10-12"
    ],
    "ecm": [
        "2019-07-19"
    ],
    "emr": [
        "2019-01-03"
    ],
    "es": [
        "2018-04-16"
    ],
    "faceid": [
        "2018-03-01"
    ],
    "gaap": [
        "2018-05-29"
    ],
    "gme": [
        "2018-07-11"
    ],
    "gpm": [
        "2020-08-20"
    ],
    "gse": [
        "2019-11-12"
    ],
    "iai": [
        "2020-03-03"
    ],
    "iotcloud": [
        "2021-04-08"
    ],
    "ip": [
        "2021-04-09"
    ],
    "kms": [
        "2019-01-18"
    ],
    "lighthouse": [
        "2020-03-24"
    ],
    "live": [
        "2018-08-01"
    ],
    "mariadb": [
        "2017-03-12"
    ],
    "mdc": [
        "2020-08-28"
    ],
    "mdl": [
        "2020-03-26"
    ],
    "mdp": [
        "2020-05-27"
    ],
    "mongodb": [
        "2019-07-25"
    ],
    "monitor": [
        "2018-07-24"
    ],
    "mps": [
        "2019-06-12"
    ],
    "msp": [
        "2018-03-19"
    ],
    "ocr": [
        "2018-11-19"
    ],
    "organization": [
        "2018-12-25"
    ],
    "postgres": [
        "2017-03-12"
    ],
    "privatedns": [
        "2020-10-28"
    ],
    "redis": [
        "2018-04-12"
    ],
    "rum": [
        "2021-06-22"
    ],
    "scf": [
        "2018-04-16"
    ],
    "ses": [
        "2020-10-02"
    ],
    "sms": [
        "2021-01-11",
        "2019-07-11"
    ],
    "sqlserver": [
        "2018-03-28"
    ],
    "ssl": [
        "2019-12-05"
    ],
    "ssm": [
        "2019-09-23"
    ],
    "sts": [
        "2018-08-13"
    ],
    "tag": [
        "2018-08-13"
    ],
    "tcaplusdb": [
        "2019-08-23"
    ],
    "tcr": [
        "2019-09-24"
    ],
    "tdmq": [
        "2020-02-17"
    ],
    "tem": [
        "2021-07-01",
        "2020-12-21"
    ],
    "tiw": [
        "2019-09-19"
    ],
    "tke": [
        "2018-05-25"
    ],
    "trtc": [
        "2019-07-22"
    ],
    "vod": [
        "2018-07-17"
    ],
    "vpc": [
        "2017-03-12"
    ],
    "yunjing": [
        "2018-02-28"
    ]
}