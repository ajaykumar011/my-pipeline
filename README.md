
# Welcome to your CDK Python project!

This example is ideal for crossregion Deployment [not CROSS-ACCOUNT DEPLOYMENT]

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
CDK Bootstrapping  for Base, Prod, Stage

#Pipeline Account (base Pipeline account)
export CDK_NEW_BOOTSTRAP=1  (for windows use set CDK_NEW_BOOTSTRAP=1)
npx cdk bootstrap --profile pipeline-ac --cloudformation-execution-policies arn:aws:iam::aws:policy/AdministratorAccess aws://304962413949/ap-south-1

#Pre-Prod  Account [App Account]
export CDK_NEW_BOOTSTRAP=1  (for windows use set CDK_NEW_BOOTSTRAP=1)
npx cdk bootstrap --profile pre-prod --cloudformation-execution-policies arn:aws:iam::aws:policy/AdministratorAccess aws://304962413949/us-east-1

#Prod Trusted Account 
export CDK_NEW_BOOTSTRAP=1  (for windows use set CDK_NEW_BOOTSTRAP=1)
npx cdk bootstrap --profile prod --cloudformation-execution-policies arn:aws:iam::aws:policy/AdministratorAccess --trust 304962413949 aws://143787628822/us-east-2
