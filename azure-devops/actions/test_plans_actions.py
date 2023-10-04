from .. import action_store as action_store
from ..azure_devops_wrapper import *
from ..models.test_plan_models import *
# from ..models.nic_models import *
from typing import Union
# import json

logger = logging.getLogger(__name__)



def create_testplan_azure_devops(params: CreateTestPlanParameters):
    try:
        api_version = "7.0"
        organization = params.organization
        project = params.project
        test_plan_data = {
                            "name": params.testplanName,
                            "description": params.testplanDescription
                            }
        endpoint = f"/{organization}/{project}/_apis/test/plans"
        response = post_wrapper_azure_devops(endpoint, api_version, data = test_plan_data)
        return response
    except Exception as e:
        logger.error(f"Failed to create testplan : {e}")
        return {"error": str(e)}

def delete_testplan_azure_devops(params: DeleteTestPlanParameters):
    try:
        api_version = "7.0"
        organization = params.organization
        project = params.project
        planId = params.planId
        endpoint = f"/{organization}/{project}/_apis/test/plans/{planId}"
        response = delete_wrapper(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to delete test plan : {e}")
        return {"error": str(e)}

def get_testplan_azure_devops(params: GetTestPlanParameters):
    try:
        api_version = "7.0"
        organization = params.organization
        project = params.project
        planId = params.planId
        endpoint = f"/{organization}/{project}/_apis/test/plans/{planId}"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to get test plan : {e}")
        return {"error": str(e)}

def list_testplan_azure_devops(params: ListTestPlanParameters):
    try:
        api_version = "7.0"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/test/plans"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to list testplans : {e}")
        return {"error": str(e)}


def create_test_runs_azure_devops(params: CreateTestRunsParameters):
    try:
        api_version = "7.0"
        organization = params.organization
        project = params.project
        test_runs_data = {
                        "name": params.runsName,
                        "plan": {
                            "id": params.planId
                        },
                        "pointIds": [
                            1,
                            2
                        ]
                        }
        endpoint = f"/{organization}/{project}/_apis/test/runs"
        response = post_wrapper_azure_devops(endpoint , api_version, data=test_runs_data)
        return response
    except Exception as e:
        logger.error(f"Failed to create test runs ] : {e}")
        return {"error": str(e)}
    
def delete_test_runs_azure_devops(params: DeleteTestRunsParameters):
    try:
        api_version = "7.0"
        organization = params.organization
        project = params.project
        runId = params.runId
        endpoint = f"/{organization}/{project}/_apis/test/runs/{runId}"
        response = delete_wrapper(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to delete test runs ] : {e}")
        return {"error": str(e)}
    
def get_test_runs_azure_devops(params: GetTestRunsParameters):
    try:
        api_version = "7.0"
        organization = params.organization
        project = params.project
        runId = params.runId
        endpoint = f"/{organization}/{project}/_apis/test/runs/{runId}"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to get test runs : {e}")
        return {"error": str(e)}
    
def list_test_runs_azure_devops(params: ListTestRunsParameters):
    try:
        api_version = "7.0"
        organization = params.organization
        project = params.project
        # runId = params.runId
        endpoint = f"/{organization}/{project}/_apis/test/runs"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to list test runs : {e}")
        return {"error": str(e)}
    
def get_test_runs_statistics_azure_devops(params: GetTestRunsStatisticsParameters):
    try:
        api_version = "7.0"
        organization = params.organization
        project = params.project
        runId = params.runId
        endpoint = f"/{organization}/{project}/_apis/test/runs/{runId}/Statistics"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to get test runs statistics : {e}")
        return {"error": str(e)}
    
def get_results_test_runs_azure_devops(params: GetTestRunsResultsParameters):
    try:
        api_version = "7.0"
        organization = params.organization
        project = params.project
        runId = params.runId
        testCaseResultId = params.testCaseResultId
        endpoint = f"/{organization}/{project}/_apis/test/Runs/{runId}/results/{testCaseResultId}"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to get results test runs statistics : {e}")
        return {"error": str(e)}
    
def list_results_test_runs_azure_devops(params: ListTestRunsResultsParameters):
    try:
        api_version = "7.0"
        organization = params.organization
        project = params.project
        runId = params.runId
        endpoint = f"/{organization}/{project}/_apis/test/Runs/{runId}/results"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to list results test runs statistics : {e}")
        return {"error": str(e)}


