from ..models.eks_models import (
    CreateClusterRequest,
    CreateClusterResponse,
    DescribeClusterRequest,
    DescribeClusterResponse,
    ListClustersRequest,
    ListClustersResponse,
)

from ..main_store import store
from ..aws_wrapper import get_resource, get_session, get_client


@store.kubiya_action()
def create_eks_cluster(request: CreateClusterRequest) -> CreateClusterResponse:
    """
    Creates an Amazon EKS cluster.

    Args:
        request (CreateClusterRequest): The request containing the details of the cluster to create.

    Returns:
        CreateClusterResponse: The response containing the details of the created cluster.
    """
    eks = get_client("eks")
    response = eks.create_cluster(**request.dict(exclude_none=True))
    cluster_name = response["cluster"]["name"]
    return CreateClusterResponse(cluster_name=cluster_name)


@store.kubiya_action()
def describe_eks_cluster(request: DescribeClusterRequest) -> DescribeClusterResponse:
    """
    Describes an Amazon EKS cluster.

    Args:
        request (DescribeClusterRequest): The request containing the name of the cluster.

    Returns:
        DescribeClusterResponse: The response containing the details of the cluster.
    """
    eks = get_client("eks")
    response = eks.describe_cluster(name=request.cluster_name)
    cluster = response["cluster"]
    return DescribeClusterResponse(cluster=cluster)


@store.kubiya_action()
def list_eks_clusters(request: ListClustersRequest) -> ListClustersResponse:
    """
    Lists the Amazon EKS clusters in the specified region.

    Args:
        request (ListClustersRequest): The request containing the optional filters.

    Returns:
        ListClustersResponse: The response containing the list of cluster names.
    """
    eks = get_client("eks")
    response = eks.list_clusters()
    clusters = response["clusters"]
    return ListClustersResponse(clusters=clusters)