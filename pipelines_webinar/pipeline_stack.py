from aws_cdk import core
from aws_cdk import aws_codepipeline as codepipeline
from aws_cdk import aws_codepipeline_actions as cpactions
from aws_cdk import pipelines

from .webservice_stage import WebServiceStage

PRE_PROD_ACCOUNT = '304962413949'  # This is pre-prod account
PROD_ACCOUNT = '143787628822'  # This is prod account

class PipelineStack(core.Stack):
  def __init__(self, scope: core.Construct, id: str, **kwargs):
    super().__init__(scope, id, **kwargs)

    source_artifact = codepipeline.Artifact()
    cloud_assembly_artifact = codepipeline.Artifact()

    pipeline = pipelines.CdkPipeline(self, 'Pipeline',
      cloud_assembly_artifact=cloud_assembly_artifact,
      pipeline_name='WebinarPipeline',

      source_action=cpactions.GitHubSourceAction(
        action_name='GitHub',
        output=source_artifact,
        oauth_token=core.SecretValue.secrets_manager('GITHUB-TOKEN'),
        owner='ajaykumar011',
        repo='my-pipeline',
        branch='main',
        trigger=cpactions.GitHubTrigger.POLL),

      synth_action=pipelines.SimpleSynthAction(
        source_artifact=source_artifact,
        cloud_assembly_artifact=cloud_assembly_artifact,
        install_command='npm install -g aws-cdk && pip install -r requirements.txt && pip install pytest',
        build_command='pytest unittests',
        synth_command='cdk synth'))

    pre_prod_app = WebServiceStage(self, 'Pre-Prod', env={
      'account': PRE_PROD_ACCOUNT,
      'region': 'ap-south-1',  #This is the same region where pipeline is
    })
    pre_prod_stage = pipeline.add_application_stage(pre_prod_app)
    pre_prod_stage.add_actions(pipelines.ShellScriptAction(
      action_name='Integ',
      run_order=pre_prod_stage.next_sequential_run_order(),
      additional_artifacts=[source_artifact],
      commands=[
        'pip install -r requirements.txt',
        'pip install requests',
        'pip install pytest',
        'pytest integtests',
      ],
      use_outputs={
        'SERVICE_URL': pipeline.stack_output(pre_prod_app.url_output)
      }))

    # pipeline.add_application_stage(WebServiceStage(self, 'Prod', env={
    #   'account': PROD_ACCOUNT,
    #   'region': 'us-east-2',
    # }))



