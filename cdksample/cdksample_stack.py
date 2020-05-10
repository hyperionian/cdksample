from aws_cdk import (
    aws_iam as iam,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    core
)

from hitcounterc import HitCounters

class CdksampleStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        the_function  = _lambda.Function(
            self, 'HelloWorld',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('functions'),
            handler='hello.handler',
        )

        hello_with_counter = HitCounters(
            self, 'HitCounterHelloFunction',
            downstream=the_function,
        )

        apigw.LambdaRestApi(
            self, 'RESTendpoint',
            handler=hello_with_counter.handler,
        )

