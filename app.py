#!/usr/bin/env python3

from aws_cdk import core

from cdksample.cdksample_stack import CdksampleStack


app = core.App()
CdksampleStack(app, "cdksample", env={'region': 'ap-southeast-2'})

app.synth()
