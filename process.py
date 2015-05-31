#!/usr/bin/env python3

import logging

from processor import sources, outputs, run_pipeline
from twiggy_goodies.setup import setup_logging
from settings import *

setup_logging('processor.log')



def if_ios(item):
    if item['data']['namespace'] == 'ios':
        return item


def if_android(item):
    if item['data']['namespace'] == 'android':
        return item


def prepare_for_slack(item):
    data = item['data']
    versions = ', '.join(v['number']
                         for v in data['versions'])
    return dict(text='{namespace}/{name} {versions}'.format(
        namespace=data['namespace'],
        name=data['name'],
        versions=versions))

    
def prepare_for_mail(item):
    data = item['data']
    versions = ', '.join(v['number']
                         for v in data['versions'])
    subject = '{namespace}/{name} {versions}'.format(
        namespace=data['namespace'],
        name=data['name'],
        versions=versions)

    # actually, some template formatter could be used here
    def format_version(v):
        return """<h1>{number}</h1>

{content}""".format(**v)

    body = '\n\n'.join(map(format_version, data['versions']))
    return dict(subject=subject,
                body=body)


run_pipeline(
    sources.web.hook(**LISTEN_ON),
    outputs.fanout(
        [if_ios, outputs.fanout(
            [prepare_for_slack, outputs.slack(IOS_TEAM_CHAT)],
            [prepare_for_mail, outputs.email(**IOS_MAILLIST)])],
        [if_android, prepare_for_slack, outputs.slack(ANDROID_TEAM_CHAT)]))
