from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from typing import List


class LambdaPublicAuthorization(BaseResourceCheck):
    def __init__(self):
        name = "Ensure lambda does not have public authorization."
        id = "CKV2_CUSTOM_037"
        supported_resources = ["aws_lambda_function_url"]
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(
            name=name,
            id=id,
            categories=categories,
            supported_resources=supported_resources,
        )

    def scan_resource_conf(self, conf):
        if "authorization_type" in conf.keys():
            authorization_type = conf["authorization_type"]
            if "AWS_IAM" in authorization_type:
                return CheckResult.PASSED
            else:
                return CheckResult.FAILED

    def get_evaluated_keys(self) -> List[str]:
        return ["authorization_type"]


check = LambdaPublicAuthorization()
