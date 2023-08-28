from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ListClustersInput(BaseModel):
    server: Optional[str] = ""
    name: Optional[str] = ""
    type_of_kubernetes_resource_like_pod_deployment_etc: Optional[str] = Field("pod", alias = "id.type")
    name_of_kubernetes_resource_like_kube_proxy_v5t6_etc: Optional[str] = Field(..., alias = "id.value")
