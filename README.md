# centralized_checkov_sast

This is the companion repository for the Centralized Custom Checkov Scanning APG which is slated for public publishing in the second half of 2023.

The code in this repository is designed to be deployed to two separate modules, though it can be deployed in one if prefered.

## Workflows

The `.github/workflows` folder contains the reusable workflow for Checkov as well as an example for how to call the reusable workflow.

## Custom Rules

The remaining content contains code that defines the Checkov custom rules and Checkov configuration.

# Checkov Custom Rules

This section provides design details for deploying a centralized Checkov configuration that can be reused in Terraform pipelines.

### Dependencies/Assumptions

The deployment of centralized Checkov SAST depends on this repo for sharing custom rule content.

This repo can be checked out during a workflow and used to run standard Checkov checks on a repository. See the `github_workflow` repo's Checkov workflow files for example usage.

### Checkov Configuration File

The file `.checkov.yml` is a Checkov configuration file that defines the parameters that should be used when running Checkov.

### Checkov Custom Checks

Checkov custom checks should be added to the `custom_policies` directory. Two example rules are added to start.

The Checkov configuration file will reference this directory to run the checks during the Checkov action.

For more details on custom checks, see: https://www.checkov.io/3.Custom%20Policies/Custom%20Policies%20Overview.html

#### Custom Check Naming Convention

Your custom check should start with `custom_`, followed by a unique three-digit number, followed by a `snake_case` description of what the check looks for.

Checks can be written in either Python or YAML.

Python checks should have a `check = <NameOfYourCheckClass>()` line at the the very bottom, not indented at all (ie. outside of the class definition).

#### Unit Testing 

To create a unit test for a Python-based custom check, do the following:

1. Create a python file ending in `_test.py` instead of just `.py`.
2. Update the `./custom_policies/test` folder with Terraform resources that represent known-good or known-bad states for your test's consumption.
3. Extend the `unittest.TestCase` class to write your unit test class (you can copy an existing unit test for the framework and update it). Add methods for each test you want to perform.
4. Run the test using the commands from the `unittest.yaml` workflow.

### Example Usage

See `checkov-scan.yaml` in the `github_workflows` directory for an example that can be added to your repo's `workflows` folder.

### Handling Checkov False Positives

Checkov false positives can be ignored in individual terraform files by adding a skip comment prior to the offending line. Just specify the Checkov ID from the warning and provide a reason why the check should not apply. For example:
```hcl
#checkov:skip=CKV_AWS_50:No need for Xray tracing
tfProperty = var.myTfVar
```

If you think a rule should be suppressed globally, create an issue in this repository and reach out to the security team to discuss adding it.

### Suggested Ownership

The Security team should own this repository and be responsible for ensuring the contents of the configuration file and custom checks.

Any developer can submit issues to the shared repository to request additional checks or exclusions that should be added universally, though it is up to the security team's discretion about whether to make those changes.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
