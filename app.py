#!/usr/bin/env python3

from aws_cdk import core
from my_pipeline.my_pipeline_stack import MyPipelineStack

app = core.App()
MyPipelineStack(app, "my-pipeline",
    env=core.Environment(account="304962413949", region="ap-south-1"))
app.synth()