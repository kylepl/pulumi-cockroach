# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetClusterCertResult',
    'AwaitableGetClusterCertResult',
    'get_cluster_cert',
    'get_cluster_cert_output',
]

@pulumi.output_type
class GetClusterCertResult:
    """
    A collection of values returned by getClusterCert.
    """
    def __init__(__self__, cert=None, id=None):
        if cert and not isinstance(cert, str):
            raise TypeError("Expected argument 'cert' to be a str")
        pulumi.set(__self__, "cert", cert)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def cert(self) -> str:
        """
        Certificate contents.
        """
        return pulumi.get(self, "cert")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Cluster ID.
        """
        return pulumi.get(self, "id")


class AwaitableGetClusterCertResult(GetClusterCertResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterCertResult(
            cert=self.cert,
            id=self.id)


def get_cluster_cert(id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterCertResult:
    """
    TLS certificate for the specified CockroachDB cluster. Certificates for dedicated clusters should be written to `$HOME/Library/CockroachCloud/certs/<cluster name>-ca.crt` on MacOS or Linux, or `$env:appdata\\CockroachCloud\\certs\\<cluster name>-ca.crt` on Windows.

    Serverless clusters use the root PostgreSQL CA cert. If it isn't already installed, the certificate can be appended to `$HOME/.postgresql/root.crt` on MacOS or Linux, or `$env:appdata\\postgresql\\root.crt` on Windows.


    :param str id: Cluster ID.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cockroach:index/getClusterCert:getClusterCert', __args__, opts=opts, typ=GetClusterCertResult).value

    return AwaitableGetClusterCertResult(
        cert=__ret__.cert,
        id=__ret__.id)


@_utilities.lift_output_func(get_cluster_cert)
def get_cluster_cert_output(id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterCertResult]:
    """
    TLS certificate for the specified CockroachDB cluster. Certificates for dedicated clusters should be written to `$HOME/Library/CockroachCloud/certs/<cluster name>-ca.crt` on MacOS or Linux, or `$env:appdata\\CockroachCloud\\certs\\<cluster name>-ca.crt` on Windows.

    Serverless clusters use the root PostgreSQL CA cert. If it isn't already installed, the certificate can be appended to `$HOME/.postgresql/root.crt` on MacOS or Linux, or `$env:appdata\\postgresql\\root.crt` on Windows.


    :param str id: Cluster ID.
    """
    ...
