from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from typing import List


class EC2TerminationProtection(BaseResourceCheck):
    def __init__(self):
        name = "Ensure that EC2 instance has termination protection enabled"
        id = "CKV2_CUSTOM_033"
        supported_resources = ["aws_instance"]
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(
            name=name,
            id=id,
            categories=categories,
            supported_resources=supported_resources,
        )

    def scan_resource_conf(self, conf):
        if "disable_api_termination" in conf.keys():
            return CheckResult.PASSED
        else:
            return CheckResult.FAILED

    def get_evaluated_keys(self) -> List[str]:
        return ["disable_api_termination"]


check = EC2TerminationProtection()
