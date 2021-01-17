#!/usr/bin/env python3

from aws_cdk import core
#from my_pipeline.my_pipeline_stack import MyPipelineStack
from pipelines_webinar.pipelines_webinar_stack import PipelinesWebinarStack
from pipelines_webinar.pipeline_stack import PipelineStack

PIPELINE_ACCOUNT = '304962413949'

app = core.App()
PipelinesWebinarStack(app, "pipeline-webinar")
PipelineStack(app, 'PipelineStack', env={
  'account': PIPELINE_ACCOUNT,
  'region': 'ap-south-1',
})

app.synth()